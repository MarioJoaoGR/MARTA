
import pytest
from unittest.mock import patch, sentinel

@pytest.fixture(autouse=True)
def setup():
    class Z:
        _get_set = sentinel.nothing
        
        @classmethod
        def get_only(cls):
            return sentinel.get_only
    
    yield Z

def test_valid_input(setup):
    z = setup()
    assert z.get_only() == sentinel.get_only
