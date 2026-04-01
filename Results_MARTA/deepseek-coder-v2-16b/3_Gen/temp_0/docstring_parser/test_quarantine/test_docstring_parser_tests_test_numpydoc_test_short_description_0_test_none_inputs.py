
import pytest
from docstring_parser import parse
import typing as T

def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    if source is not None:
        docstring = parse(source)
        assert docstring.short_description == expected
        assert docstring.long_description is None
        assert not docstring.meta
    else:
        with pytest.raises(TypeError):
            parse(source)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_short_description_0_test_none_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_short_description_0_test_none_inputs.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""