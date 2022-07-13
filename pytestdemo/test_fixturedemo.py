import pytest


@pytest.fixture()
def launch():
    print("First launch browser")
    yield
    print("close browser after task perform")


def test_fixturedmo(launch):
    print("executing after launch method")
