
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture(name='httpie_parser')
def create_httpie_parser():
    return HTTPieArgumentParser()

def test_edge_cases(httpie_parser):
    with pytest.raises(AttributeError):
        httpie_parser._body_from_input("test data")
