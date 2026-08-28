
import pytest
from apimd.parser import Parser

def setup_parser_with_constants():
    parser = Parser()
    parser.const['pkg_name.CONST1'] = 'type1'
    parser.root['pkg_name.CONST1'] = 'pkg_name'
    return parser

def setup_parser_without_constants():
    parser = Parser()
    return parser


def test_no_constants():
    parser = setup_parser_without_constants()
    constants_table = parser._Parser__get_const('pkg_name')
    expected_output = ""
    assert constants_table == expected_output