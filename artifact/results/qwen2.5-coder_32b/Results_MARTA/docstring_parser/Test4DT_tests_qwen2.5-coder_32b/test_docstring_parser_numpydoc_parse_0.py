
import pytest
from docstring_parser.numpydoc import parse, Docstring

def test_valid_case():
    docstring_text = """This function adds two numbers.
    
    Parameters
    ----------
    a : int
        The first number to add.
    b : int
        The second number to add.
    
    Returns
    -------
    int
        The sum of the two numbers."""
    
    parsed_doc = parse(docstring_text)
    assert parsed_doc.short_description == "This function adds two numbers."
    assert len(parsed_doc.meta) == 3

def test_valid_case_with_long_description():
    docstring_text = """This function adds two numbers.
    
    Detailed description on how this function works and its purpose.
    It takes two integers as input and returns their sum.
    
    Parameters
    ----------
    a : int
        The first number to add.
    b : int
        The second number to add.
    
    Returns
    -------
    int
        The sum of the two numbers."""
    
    parsed_doc = parse(docstring_text)
    assert parsed_doc.short_description == "This function adds two numbers."
    assert len(parsed_doc.meta) == 3

def test_valid_case_with_examples():
    docstring_text = """This function adds two numbers.
    
    Parameters
    ----------
    a : int
        The first number to add.
    b : int
        The second number to add.
    
    Returns
    -------
    int
        The sum of the two numbers.
    
    Examples
    --------
    >>> add(1, 2)
    3"""
    
    parsed_doc = parse(docstring_text)
    assert parsed_doc.short_description == "This function adds two numbers."
    assert len(parsed_doc.meta) == 4

def test_valid_case_with_multiline_param_description():
    docstring_text = """This function adds two numbers.
    
    Parameters
    ----------
    a : int
        The first number to add.
        It can be any integer value.
    b : int
        The second number to add.
        It can also be any integer value.
    
    Returns
    -------
    int
        The sum of the two numbers."""
    
    parsed_doc = parse(docstring_text)
    assert parsed_doc.short_description == "This function adds two numbers."
    assert len(parsed_doc.meta) == 3

def test_valid_case_with_multiline_return_description():
    docstring_text = """This function adds two numbers.
    
    Parameters
    ----------
    a : int
        The first number to add.
    b : int
        The second number to add.
    
    Returns
    -------
    int
        The sum of the two numbers.
        This is a detailed description of what the return value represents."""
    
    parsed_doc = parse(docstring_text)
    assert parsed_doc.short_description == "This function adds two numbers."
    assert len(parsed_doc.meta) == 3
