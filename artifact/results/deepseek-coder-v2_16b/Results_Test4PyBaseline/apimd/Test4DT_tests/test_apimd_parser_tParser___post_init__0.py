
# Module: apimd.parser
# test_parser.py
from apimd.parser import Parser
import pytest

@pytest.fixture
def parser():
    return Parser()

@pytest.fixture
def parameterized_parser():
    return Parser.new(link=True, level=1, toc=False)

def test_default_settings(parser):
    assert parser.link is True
    assert parser.b_level == 1
    assert parser.toc is False

def test_parameterized_settings(parameterized_parser):
    assert parameterized_parser.link is True
    assert parameterized_parser.b_level == 1
    assert parameterized_parser.toc is False

@pytest.mark.parametrize("link, b_level, toc", [
    (True, 1, False),
    (False, 2, True),
    (True, 3, False)
])
def test_multiple_settings(link, b_level, toc):
    p = Parser.new(link=link, level=b_level, toc=toc)