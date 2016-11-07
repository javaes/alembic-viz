import sys

from alembic.config import Config
from alembic.util import CommandError
import click

from utils import get_revisions
from utils import generate_revision_graph

VALID_OUTPUT_FORMATS = ['png', 'svg', 'pdf']

@click.command()
@click.option('--config', default='alembic.ini', help='path to alembic config file')
@click.option('--name', default='alembic', help='name of the alembic ini section')
@click.option('--filename', default='migrations', help='output file name without file extension')
@click.option('--format', default='png', help='output file format',
              type=click.Choice(VALID_OUTPUT_FORMATS))
def cli(config, name, filename, format):
    alembic_config = Config(file_=config, ini_section=name)
    try:
        revisions = get_revisions(alembic_config)
    except CommandError as e:
        sys.exit(e)
    dot = generate_revision_graph(revisions, format)
    dot.render(filename=filename)


if __name__ == '__main__':
    cli()
