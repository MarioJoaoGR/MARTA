
from docstring_parser.tests.test_epydoc import compose, parse

def test_empty_input():
    source = ""
    expected = ""
    assert compose(parse(source)) == expected
