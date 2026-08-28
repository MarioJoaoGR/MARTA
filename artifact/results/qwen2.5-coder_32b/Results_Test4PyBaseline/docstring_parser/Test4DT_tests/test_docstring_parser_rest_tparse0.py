# Module: docstring_parser.rest
import pytest
from docstring_parser.rest import parse
from docstring_parser import Docstring

def test_parse_simple_docstring():
    text = "This function adds two numbers.\n:param int x: The first number."
    doc = parse(text)
    assert doc.short_description == "This function adds two numbers."
    assert len(doc.meta) == 1
    assert doc.meta[0].arg_name == "x"
    assert doc.meta[0].type_name == "int"

def test_parse_docstring_with_long_description():
    text = ("This function divides two numbers.\n\nThe division is performed element-wise."
            "\n:returns float: The result of the division.\n:raises ZeroDivisionError: If the divisor is zero.")
    doc = parse(text)
    assert doc.short_description == "This function divides two numbers."
    assert doc.long_description == "The division is performed element-wise."
    assert len(doc.meta) == 2
    assert doc.meta[0].type_name == "float"
    assert doc.meta[1].type_name == "ZeroDivisionError"

def test_parse_empty_docstring():
    text = ""
    doc = parse(text)
    assert doc.short_description is None
    assert doc.long_description is None
    assert len(doc.meta) == 0

def test_parse_only_metadata_entries():
    text = ":param str name: The name of the user.\n:returns bool: True if successful."
    doc = parse(text)
    assert doc.short_description is None
    assert doc.long_description is None
    assert len(doc.meta) == 2
    assert doc.meta[0].arg_name == "name"
    assert doc.meta[1].type_name == "bool"

def test_parse_multiple_parameters():
    text = ("This function calculates the area of a rectangle."
            "\n:param float width: The width of the rectangle."
            "\n:param float height: The height of the rectangle.")
    doc = parse(text)
    assert doc.short_description == "This function calculates the area of a rectangle."
    assert len(doc.meta) == 2
    assert doc.meta[0].arg_name == "width"
    assert doc.meta[1].type_name == "float"

def test_parse_blank_lines():
    text = ("This function does something.\n\n\n:param int y: The second number.")
    doc = parse(text)
    assert doc.short_description == "This function does something."
    assert doc.blank_after_short_description is True
    assert len(doc.meta) == 1

def test_parse_no_metadata():
    text = "This function has no metadata.\nIt just does something."
    doc = parse(text)
    assert doc.short_description == "This function has no metadata."
    assert doc.long_description == "It just does something."
    assert len(doc.meta) == 0
