import os
import subprocess

import click


@click.command()
@click.argument('path', default=os.path.join('dicegame', 'tests'))
def cli(path):
    """
    Run tests with Pytest.

    Args:
        (path) Test path
        (return) Subprocess call result
    """
    cmd = 'pytest {0}'.format(path)
    return subprocess.call(cmd, shell=True)
