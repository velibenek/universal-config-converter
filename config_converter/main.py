import click
from .converter import convert

@click.command()
@click.option('--input-file', '-i', required=True, type=click.Path(exists=True, dir_okay=False), help='Path to the input configuration file.')
@click.option('--source-format', '-s', required=True, type=click.Choice(['json', 'yaml', 'toml', 'env', 'ini', 'xml'], case_sensitive=False), help='Format of the input file.')
@click.option('--target-format', '-t', required=True, type=click.Choice(['json', 'yaml', 'toml', 'env', 'ini', 'xml'], case_sensitive=False), help='Format for the output file.')
@click.option('--output-file', '-o', required=True, type=click.Path(dir_okay=False), help='Path to save the converted configuration file.')
def main(input_file, source_format, target_format, output_file):
    """Universal Config Converter CLI"""
    try:
        convert(input_file, source_format, target_format, output_file)
        click.echo(f"Successfully converted '{input_file}' ({source_format}) to '{output_file}' ({target_format})")
    except Exception as e:
        click.echo(f"Error during conversion: {e}", err=True)

if __name__ == '__main__':
    main()
