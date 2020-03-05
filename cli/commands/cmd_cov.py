import subprocess

import click


@click.command()
@click.argument('path', default='dicegame')
def cli(path):
    """
    Run a test coverage report.

    Args:
        (path) Test path
        (return) Subprocess call result
    """
    cmd = 'pytest --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)
