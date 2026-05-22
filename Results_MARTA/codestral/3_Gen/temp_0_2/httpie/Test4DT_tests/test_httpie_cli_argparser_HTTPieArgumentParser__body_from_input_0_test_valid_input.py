
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_valid_input(parser):
    with pytest.raises(TypeError):
        parser._body_from_input()
