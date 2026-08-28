
import pytest
from apimd.parser import Parser


def test_no_alias():
    p = Parser()
    p.doc = {'sec1': 'content1', 'sec2': 'content2'}
    p.alias = {}
    p.root = {'sec1': 'root_sec1'}
    
    # Call the method under test
    p._Parser__find_alias()
    
    # Assert that no changes were made to the doc dictionary
    assert p.doc == {'sec1': 'content1', 'sec2': 'content2'}

def test_invalid_alias():
    p = Parser()
    p.doc = {'sec1': 'content1', 'sec2': 'content2'}
    p.alias = {'alias1': 'nonexistent_sec'}
    p.root = {'sec1': 'root_sec1'}
    
    # Call the method under test
    p._Parser__find_alias()
    
    # Assert that no changes were made to the doc dictionary
    assert p.doc == {'sec1': 'content1', 'sec2': 'content2'}

def test_non_immediate_family():
    p = Parser()
    p.doc = {'sec1.child': 'content1', 'sec2': 'content2'}
    p.alias = {'alias1': 'sec1'}
    p.root = {'sec1.child': 'root_sec1.child'}
    
    # Call the method under test
    p._Parser__find_alias()
    
    # Assert that no changes were made to the doc dictionary
    assert p.doc == {'sec1.child': 'content1', 'sec2': 'content2'}
