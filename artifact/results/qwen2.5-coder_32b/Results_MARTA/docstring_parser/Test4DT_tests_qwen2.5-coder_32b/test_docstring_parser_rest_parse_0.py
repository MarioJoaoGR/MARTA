
import re
import inspect
from docstring_parser.rest import parse, Docstring

def test_parse_basic():
    raw_docstring = """
    This function adds two numbers.

    The function takes two integer parameters and returns their sum.
    :param a: int? The first number to add. Defaults to 0.
    :param b: int? The second number to add. Defaults to 0.
    :return: int The sum of the two numbers.
    """
    parsed_doc = parse(raw_docstring)
    
    assert parsed_doc.short_description == "This function adds two numbers."
    assert parsed_doc.long_description == "The function takes two integer parameters and returns their sum."
