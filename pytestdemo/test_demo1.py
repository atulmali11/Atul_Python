# Any pytest file should start with test_ .
#pytest methods name should start with test
# Any code should wrapped in method
import pytest


@pytest.mark.smoke
def test_firstprogram1():
    print("Hello")

@pytest.mark.xfail
def test_secondprogram2():
    print("Atul Mali")