
# Module: docstring_parser.tests.test_numpydoc
# Import the function to be tested
from docstring_parser import parse
import typing as T

def test_default_args():
    # Test case 1: Function with an optional parameter and a default value
    source = """
    def example(param1: int = 5):
        pass
    """
    expected_is_optional = False
    expected_type_name = "int"
    expected_default = "5"
    
    docstring = parse(source)
    assert docstring is not None