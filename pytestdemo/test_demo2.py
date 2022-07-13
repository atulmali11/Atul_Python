import pytest


@pytest.mark .smoke
@pytest.mark.skip
def test_firstprogram():
   msg ="Hello"
   assert msg=='Hi', "Test failed because of not match"


def test_secondprogram():
   a=5
   b=4
   assert a+2==7 ,"Addition match"