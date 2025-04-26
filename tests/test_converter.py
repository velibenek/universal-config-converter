import pytest
import json
import yaml
import toml
from config_converter.converter import convert, load_config, save_config
from dotenv import dotenv_values
import configparser
import xmltodict

# Sample data for testing
SAMPLE_DATA = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "test_user",
        "enabled": True,
    },
    "api_settings": {"key": "abcdef12345", "retries": 3},
    "feature_flags": ["new_ui", "beta_feature"],
}

# Sample data specifically for .env testing (flat structure)
FLAT_SAMPLE_DATA = {
    "API_KEY": "abcdef12345",
    "DATABASE_HOST": "db.example.com",
    "DATABASE_PORT": "5432",  # .env values are typically strings
    "DEBUG_MODE": "true",
    "TIMEOUT_SECONDS": "30",
}

# Sample data specifically for INI testing (sections)
INI_SAMPLE_DATA = {
    "database": {"host": "db.example.com", "port": "1521", "enabled": "true"},
    "user_settings": {"theme": "dark", "notifications": "false"},
}

# Sample data specifically for XML testing
# Note: xmltodict converts numbers and booleans back to strings often
# Need to be careful with type comparisons
XML_SAMPLE_STR = """<?xml version="1.0" encoding="utf-8"?>
<config>
  <database host="localhost">
    <port>5432</port>
    <user>xml_user</user>
    <enabled>true</enabled>
  </database>
  <api key="key-from-xml">
    <retries>5</retries>
  </api>
  <flags>
    <flag>xml_flag1</flag>
    <flag>xml_flag2</flag>
  </flags>
</config>"""

XML_SAMPLE_DATA_FROM_STR = {
    "config": {
        "database": {
            "@host": "localhost",
            "port": "5432",
            "user": "xml_user",
            "enabled": "true",
        },
        "api": {"@key": "key-from-xml", "retries": "5"},
        "flags": {"flag": ["xml_flag1", "xml_flag2"]},
    }
}


@pytest.fixture
def temp_files(tmp_path):
    """Fixture to create temporary files for testing."""
    paths = {
        "json_in": tmp_path / "input.json",
        "yaml_in": tmp_path / "input.yaml",
        "toml_in": tmp_path / "input.toml",
        "env_in": tmp_path / "input.env",
        "ini_in": tmp_path / "input.ini",
        "xml_in": tmp_path / "input.xml",  # Add xml input
        "out": tmp_path / "output",
    }
    # Create initial files
    with open(paths["json_in"], "w") as f:
        json.dump(SAMPLE_DATA, f, indent=4)
    with open(paths["yaml_in"], "w") as f:
        yaml.dump(SAMPLE_DATA, f, default_flow_style=False)
    with open(paths["toml_in"], "w") as f:
        toml.dump(SAMPLE_DATA, f)
    # Create sample .env file
    with open(paths["env_in"], "w") as f:
        for key, value in FLAT_SAMPLE_DATA.items():
            f.write(f"{key}={value}\n")
    # Create sample .ini file
    config = configparser.ConfigParser()
    for section, data in INI_SAMPLE_DATA.items():
        config[section] = data
    with open(paths["ini_in"], "w") as f:
        config.write(f)
    # Create sample .xml file
    with open(paths["xml_in"], "w", encoding="utf-8") as f:
        f.write(XML_SAMPLE_STR)
    return paths


def test_json_to_yaml(temp_files):
    """Test converting JSON to YAML."""
    output_path = temp_files["out"].with_suffix(".yaml")
    convert(temp_files["json_in"], "json", "yaml", output_path)
    assert output_path.exists()
    loaded_data = load_config(output_path, "yaml")
    # YAML loads integers as strings sometimes depending on representation, normalize for comparison
    assert json.loads(json.dumps(loaded_data)) == SAMPLE_DATA


def test_yaml_to_toml(temp_files):
    """Test converting YAML to TOML."""
    output_path = temp_files["out"].with_suffix(".toml")
    convert(temp_files["yaml_in"], "yaml", "toml", output_path)
    assert output_path.exists()
    loaded_data = load_config(output_path, "toml")
    assert loaded_data == SAMPLE_DATA


def test_toml_to_json(temp_files):
    """Test converting TOML to JSON."""
    output_path = temp_files["out"].with_suffix(".json")
    convert(temp_files["toml_in"], "toml", "json", output_path)
    assert output_path.exists()
    loaded_data = load_config(output_path, "json")
    assert loaded_data == SAMPLE_DATA


def test_same_format_error(temp_files):
    """Test that converting to the same format raises an error."""
    output_path = temp_files["out"].with_suffix(".json")
    with pytest.raises(
        ValueError, match="Source and target formats cannot be the same."
    ):
        convert(temp_files["json_in"], "json", "json", output_path)


def test_unsupported_source_format_error(temp_files):
    """Test loading an unsupported format raises an error."""
    with pytest.raises(ValueError, match="Unsupported source format: unknown"):
        load_config(
            temp_files["json_in"], "unknown"
        )  # File content doesn't matter here


def test_unsupported_target_format_error(temp_files):
    """Test saving to an unsupported format raises an error."""
    output_path = temp_files["out"].with_suffix(".unknown")
    with pytest.raises(ValueError, match="Unsupported target format: unknown"):
        save_config(SAMPLE_DATA, output_path, "unknown")


def test_env_to_json(temp_files):
    """Test converting .env to JSON."""
    output_path = temp_files["out"].with_suffix(".json")
    convert(temp_files["env_in"], "env", "json", output_path)
    assert output_path.exists()
    loaded_data = load_config(output_path, "json")
    # .env values are loaded as strings by dotenv_values
    assert loaded_data == FLAT_SAMPLE_DATA


def test_json_to_env(temp_files):
    """Test converting JSON to .env (only top-level simple values)."""
    # Create a simplified JSON input for this test
    simple_json_path = temp_files["json_in"].parent / "simple.json"
    simple_data = {
        "SERVICE_URL": "https://api.example.com",
        "RETRIES": 5,
        "ENABLED": False,
        "FLOAT_VAL": 1.23,
        "NESTED": {"a": 1},  # This should be ignored
        "LIST_VAL": [1, 2],  # This should be ignored
    }
    expected_env_data = {
        "SERVICE_URL": "https://api.example.com",
        "RETRIES": "5",
        "ENABLED": "false",
        "FLOAT_VAL": "1.23",
        # Nested and List are excluded
    }
    with open(simple_json_path, "w") as f:
        json.dump(simple_data, f, indent=4)

    output_path = temp_files["out"].with_suffix(".env")
    convert(simple_json_path, "json", "env", output_path)
    assert output_path.exists()

    # Load the created .env file
    loaded_data = dotenv_values(output_path)

    assert loaded_data == expected_env_data


def test_ini_to_json(temp_files):
    """Test converting INI to JSON."""
    output_path = temp_files["out"].with_suffix(".json")
    convert(temp_files["ini_in"], "ini", "json", output_path)
    assert output_path.exists()
    loaded_data = load_config(output_path, "json")
    # configparser reads all values as strings
    assert loaded_data == INI_SAMPLE_DATA


def test_json_to_ini(temp_files):
    """Test converting JSON (with structure similar to INI) to INI."""
    # Use SAMPLE_DATA which has nested dicts suitable for INI sections
    input_path = temp_files["json_in"]
    output_path = temp_files["out"].with_suffix(".ini")
    convert(input_path, "json", "ini", output_path)
    assert output_path.exists()

    # Load the created INI file
    config = configparser.ConfigParser()
    config.read(output_path)
    loaded_data = {
        section: dict(config.items(section)) for section in config.sections()
    }

    # Prepare expected data: Convert all values from SAMPLE_DATA to strings
    expected_ini_data = {}
    for section, data in SAMPLE_DATA.items():
        if isinstance(data, dict):
            expected_ini_data[section] = {k: str(v) for k, v in data.items()}
        # Skip non-dict top-level items like 'feature_flags' in SAMPLE_DATA for INI

    assert loaded_data == expected_ini_data


def test_xml_to_json(temp_files):
    """Test converting XML to JSON."""
    output_path = temp_files["out"].with_suffix(".json")
    convert(temp_files["xml_in"], "xml", "json", output_path)
    assert output_path.exists()
    # Load the JSON and compare with the expected dictionary structure from XML
    with open(output_path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    assert loaded_data == XML_SAMPLE_DATA_FROM_STR


def test_json_to_xml(temp_files):
    """Test converting JSON to XML."""
    # Use a dictionary structure that translates well to XML
    json_data_for_xml = {
        "app_config": {
            "server": {"@id": "main", "#text": "192.168.1.100"},
            "port": "8080",
            "features": {"feature": ["A", "B"]},
        }
    }
    json_input_path = temp_files["out"].parent / "input_for_xml.json"
    with open(json_input_path, "w", encoding="utf-8") as f:
        json.dump(json_data_for_xml, f, indent=4)

    output_path = temp_files["out"].with_suffix(".xml")
    convert(json_input_path, "json", "xml", output_path)
    assert output_path.exists()

    # Load the created XML and convert back to dict to compare
    # This verifies the structure is preserved reasonably well
    with open(output_path, "r", encoding="utf-8") as f:
        loaded_data = xmltodict.parse(f.read())

    # Comparing dicts is easier than comparing XML strings
    assert loaded_data == json_data_for_xml
