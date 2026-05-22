
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Passing an invalid argument type to trigger TypeError
        parser = HTTPieArgumentParser(some_invalid_argument="value")
