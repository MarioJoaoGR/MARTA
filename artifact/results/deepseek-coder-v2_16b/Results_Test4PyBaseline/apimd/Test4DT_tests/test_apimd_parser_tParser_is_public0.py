
# Module: apimd.parser
# test_parser.py
from apimd.parser import Parser
import pytest
try:  # Assuming this module exists for the chain function used in the `is_public` method
    from chain import chain
except ImportError:
    pass

@pytest.fixture
def parser():
    return Parser()

def test_initialization(parser):
    assert parser.link is True
    assert parser.b_level == 1
    assert parser.toc is False
    assert isinstance(parser.level, dict)
    assert isinstance(parser.doc, dict)
    assert isinstance(parser.docstring, dict)
    assert isinstance(parser.imp, dict)
    assert isinstance(parser.root, dict)
    assert isinstance(parser.alias, dict)