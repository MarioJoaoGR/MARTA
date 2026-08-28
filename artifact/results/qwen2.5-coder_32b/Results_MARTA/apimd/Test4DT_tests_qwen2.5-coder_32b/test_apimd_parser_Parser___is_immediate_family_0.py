
import pytest
from apimd.parser import Parser







def test_valid_immediate_family():
    parser_instance = Parser(link=True, b_level=1, toc=False)
    parser_instance.root = {'module.ClassName': 'module'}
    n1 = 'module'
    n2 = 'module.ClassName'
    assert parser_instance._Parser__is_immediate_family(n1, n2) is True

def test_non_immediate_family():
    parser_instance = Parser(link=True, b_level=1, toc=False)
    parser_instance.root = {'other.module.ClassName': 'other.module'}
    n1 = 'module'
    n2 = 'other.module.ClassName'
    assert parser_instance._Parser__is_immediate_family(n1, n2) is False