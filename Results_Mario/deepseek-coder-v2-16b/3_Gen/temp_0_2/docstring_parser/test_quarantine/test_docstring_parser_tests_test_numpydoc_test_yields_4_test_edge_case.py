
import pytest
from docstring_parser import parse

def test_yields() -> None:
    """Test parsing yields."""
    docstring = parse(
        """
        Short description
        Yields
        ------
        int
            description
        """
    )
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["yields"]
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[0].description == "description"
    assert docstring.meta[0].return_name is None
    assert docstring.meta[0].is_generator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_yields_4_test_edge_case
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_yields_4_test_edge_case.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""