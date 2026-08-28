
import pytest
from apimd.parser import Parser

def test_default_initialization():
    parser = Parser()
    assert isinstance(parser, Parser)
    assert parser.link is True
    assert parser.b_level == 1
    assert parser.toc is False
    assert parser.level == {}
    assert parser.doc == {}
    assert parser.docstring == {}
    assert parser.imp == {}
    assert parser.root == {}
    assert parser.alias == {}
    assert parser.const == {}



def test_new_method():
    with pytest.raises(TypeError):
        p = Parser.new(link=True, level=1)