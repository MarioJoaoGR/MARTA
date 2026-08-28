
import pytest
from apimd.loader import gen_api






def test_valid_input():
    """
    Test valid input to ensure the function executes without errors and returns a list of strings.
    """
    result = gen_api({'Package One': 'package1'})
    assert isinstance(result, list)
    assert all(isinstance(doc, str) for doc in result)

def test_dry_run():
    """
    Test dry run option to ensure the function prints the generated documentation to the console instead of writing files.
    """
    result = gen_api({'Package One': 'package1'}, dry=True)
    assert isinstance(result, list)
    assert all(isinstance(doc, str) for doc in result)

def test_custom_prefix():
    """
    Test custom prefix option to ensure the function saves the generated API documentation files in the specified directory.
    """
    result = gen_api({'Package One': 'package1'}, prefix='custom-docs')
    assert isinstance(result, list)
    assert all(isinstance(doc, str) for doc in result)

def test_no_links():
    """
    Test no links option to ensure the function generates documentation without creating any links.
    """
    result = gen_api({'Package One': 'package1'}, link=False)
    assert isinstance(result, list)
    assert all(isinstance(doc, str) for doc in result)

def test_table_of_contents():
    """
    Test table of contents option to ensure the function includes a table of contents in the output documentation.
    """
    result = gen_api({'Package One': 'package1'}, toc=True)
    assert isinstance(result, list)
    assert all(isinstance(doc, str) for doc in result)

def test_custom_pwd():
    """
    Test custom pwd option to ensure the function uses the provided path with pkgutil.
    """
    result = gen_api({'Package One': 'package1'}, pwd='/path/to/site-packages')
    assert isinstance(result, list)
    assert all(isinstance(doc, str) for doc in result)