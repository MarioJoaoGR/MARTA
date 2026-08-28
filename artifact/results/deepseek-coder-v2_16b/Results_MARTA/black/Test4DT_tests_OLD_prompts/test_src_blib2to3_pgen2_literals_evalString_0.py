
import pytest
from blib2to3.pgen2.literals import evalString



def test_empty_string():
    with pytest.raises(AssertionError):
        evalString('')