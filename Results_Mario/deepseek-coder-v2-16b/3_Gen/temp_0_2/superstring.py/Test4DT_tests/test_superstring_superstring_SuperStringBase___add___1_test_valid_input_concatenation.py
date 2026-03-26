
import pytest
from superstring.superstring import SuperString, SuperStringConcatenation, SuperStringBase

@pytest.fixture
def setup():
    s1 = SuperString('Hello')
    s2 = SuperString(' World')
    return s1, s2

def test_valid_input_concatenation(setup):
    s1, s2 = setup
    result = s1.__add__(s2)
    assert str(result) == "Hello World"
