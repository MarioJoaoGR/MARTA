
from docstring_parser.tests.test_numpydoc import NumpydocParser

def test_other_params() -> None:
    """Test parsing other parameters in a numpy-style docstring."""
    parser = NumpydocParser()
    docstring = parser.parse("""
        Short description
        Other Parameters
        ----------------
        only_seldom_used_keywords : type, optional
            Explanation
        common_parameters_listed_above : type, optional
            Explanation
    """)
    
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == ["only_seldom_used_keywords"]
    assert docstring.meta[0].arg_name == "only_seldom_used_keywords"
    assert docstring.meta[0].type_name == "type"
    assert docstring.meta[0].is_optional is True
    assert docstring.meta[0].description == "Explanation"

    assert docstring.meta[1].args == ["common_parameters_listed_above"]
    assert docstring.meta[1].arg_name == "common_parameters_listed_above"
    assert docstring.meta[1].type_name == "type"
    assert docstring.meta[1].is_optional is True
    assert docstring.meta[1].description == "Explanation"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_other_params_2_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_other_params_2_test_valid_input.py:2:0: E0611: No name 'NumpydocParser' in module 'docstring_parser.tests.test_numpydoc' (no-name-in-module)


"""