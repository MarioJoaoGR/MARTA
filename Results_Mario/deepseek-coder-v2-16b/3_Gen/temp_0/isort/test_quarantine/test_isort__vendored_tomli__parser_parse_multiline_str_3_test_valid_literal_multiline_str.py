
from isort._vendored.tomli._parser import parse_multiline_str
from isort._vendored.tomli._constants import ILLEGAL_MULTILINE_LITERAL_STR_CHARS
from isort._vendored.tomli.Pos import Pos
import pytest
from typing import Tuple

def test_valid_literal_multiline_str():
    src = "'''This is a multiline\nliteral string'''"
    pos = Pos(0)
    literal = True
    
    result = parse_multiline_str(src, pos, literal=literal)
    
    assert result == (len(src), "This is a multiline\nliteral string")

def test_valid_basic_multiline_str():
    src = '"""This is a multiline\nbasic string"""'
    pos = Pos(0)
    literal = False
    
    result = parse_multiline_str(src, pos, literal=literal)
    
    assert result == (len(src), "This is a multiline\nbasic string")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_literal_multiline_str
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_literal_multiline_str.py:3:0: E0401: Unable to import 'isort._vendored.tomli._constants' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_literal_multiline_str.py:3:0: E0611: No name '_constants' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_literal_multiline_str.py:4:0: E0401: Unable to import 'isort._vendored.tomli.Pos' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_literal_multiline_str.py:4:0: E0611: No name 'Pos' in module 'isort._vendored.tomli' (no-name-in-module)


"""