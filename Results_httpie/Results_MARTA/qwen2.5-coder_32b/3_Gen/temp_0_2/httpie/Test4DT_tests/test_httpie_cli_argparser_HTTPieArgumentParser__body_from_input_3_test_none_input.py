
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

def test_none_input():
    parser = HTTPieArgumentParser()
    with pytest.raises(AttributeError):
        parser._body_from_input(None)
