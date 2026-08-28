
import pytest
from apimd.parser import Parser



def test_no_matching_alias():
    parser = Parser()
    parser.alias = {'alias1': 'section3'}
    parser.doc = {'section1.subsec': 'content', 'section2': 'other content'}
    parser._Parser__find_alias()
    assert 'alias1subsec' not in parser.doc


def test_no_aliases():
    parser = Parser()
    parser.alias = {}
    parser.doc = {'section1.subsec': 'content', 'section2': 'other content'}
    parser._Parser__find_alias()
    assert 'alias1subsec' not in parser.doc