
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid inputs by passing incorrect types or values to the constructor
        parser = HTTPieArgumentParser(some_invalid_argument="invalid")
