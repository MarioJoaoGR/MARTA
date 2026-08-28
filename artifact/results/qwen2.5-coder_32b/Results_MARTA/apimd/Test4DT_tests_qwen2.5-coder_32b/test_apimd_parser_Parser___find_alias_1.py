
import pytest
from apimd.parser import Parser



def test_no_matching_alias():
    p = Parser()
    p.doc = {'section1': 'content1', 'section2': 'content2'}
    p.alias = {'alias1': 'nonexistent_section'}
    p.root = {'section1': 'root.', 'section2': 'root.'}

    p._Parser__find_alias()

    assert 'alias1section1' not in p.doc
    assert 'alias1nonexistent_section' not in p.doc


def test_no_aliases():
    p = Parser()
    p.doc = {'section1': 'content1', 'section2': 'content2'}
    p.alias = {}
    p.root = {'section1': 'root.', 'section2': 'root.'}

    p._Parser__find_alias()

    assert 'alias1section1' not in p.doc
    assert 'alias2section2' not in p.doc