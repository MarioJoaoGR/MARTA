
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

def test_edge_cases():
    parser = HTTPieArgumentParser()
    with pytest.raises(AttributeError):
        parser._body_from_file(None)
