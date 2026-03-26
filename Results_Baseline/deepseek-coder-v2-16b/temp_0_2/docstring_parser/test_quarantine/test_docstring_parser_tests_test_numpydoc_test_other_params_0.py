
# Module: docstring_parser.tests.test_numpydoc
import pytest
from your_module import parse, test_other_params

def test_other_params():
    """Test parsing other parameters."""
    docstring = parse(
        """
        Short description
        Other Parameters
        ----------------
        only_seldom_used_keywords : type, optional
            Explanation
        common_parameters_listed_above : type, optional
            Explanation
        """
    )
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == ["other_param", "only_seldom_used_keywords"]
    assert docstring.meta[0].arg_name == "only_seldom_used_keywords"
    assert docstring.meta[0].type_name == "type"
    assert docstring.meta[0].is_optional is True
    assert docstring.meta[0].description == "Explanation"

    assert docstring.meta[1].args == ["other_param", "common_parameters_listed_above"]
    assert docstring.meta[1].arg_name == "common_parameters_listed_above"
    assert docstring.meta[1].type_name == "type"
    assert docstring.meta[1].is_optional is True
    assert docstring.meta[1].description == "Explanation"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_other_params_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_other_params_0.py:4:0: E0401: Unable to import 'your_module' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_other_params_0.py:6:0: E0102: function already defined line 4 (function-redefined)

"""