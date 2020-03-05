import pytest

from dicegame.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.
    Returns: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
    }

    _app = create_app(settings_override=params)
    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    Args(app): Pytest fixture
    Return: Flask app client
    """
    yield app.test_client()
