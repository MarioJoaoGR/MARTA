
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

def test_valid_input():
    parser = HTTPieArgumentParser()
    data = "valid input"
    with pytest.raises(AttributeError):
        parser._body_from_input(data)
