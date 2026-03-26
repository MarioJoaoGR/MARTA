
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse
import typing as T

def test_default_args():
    # Test case 1: Function with a required parameter (no default value)
    source = """
    def example(param1: int):
        pass
    """
    expected_is_optional = False
    expected_type_name = "int"
    expected_default = None
    
    docstring = parse(source)
    assert docstring is not None