
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_valid_input(parser):
    data = "valid input"
    with pytest.raises(AttributeError):
        parser._body_from_input(data)
