
from docstring_parser.tests.test_google import parse

def test_attributes() -> None:
    """Test parsing attributes."""
    # Test with empty docstring
    docstring = parse("Short description")
    assert len(docstring.params) == 0

    # Test with multi-line attribute descriptions
    docstring = parse(
        """
        Short description

        Attributes:
            name: description 1
                with multi-line text
            priority (int): description 2
            sender (str?): description 3
            ratio (Optional[float], optional): description 4
        """
    )
    assert len(docstring.params) == 4
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1 with multi-line text"
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
    assert docstring.params[2].arg_name == "sender"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description == "description 3"
    assert docstring.params[2].is_optional
    assert docstring.params[3].arg_name == "ratio"
    assert docstring.params[3].type_name == "Optional[float]"
    assert docstring.params[3].description == "description 4"
    assert docstring.params[3].is_optional

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_attributes_1_test_valid_input_multi_line.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_attributes ________________________________

    def test_attributes() -> None:
        """Test parsing attributes."""
        # Test with empty docstring
        docstring = parse("Short description")
        assert len(docstring.params) == 0
    
        # Test with multi-line attribute descriptions
        docstring = parse(
            """
            Short description
    
            Attributes:
                name: description 1
                    with multi-line text
                priority (int): description 2
                sender (str?): description 3
                ratio (Optional[float], optional): description 4
            """
        )
        assert len(docstring.params) == 4
        assert docstring.params[0].arg_name == "name"
        assert docstring.params[0].type_name is None
>       assert docstring.params[0].description == "description 1 with multi-line text"
E       AssertionError: assert 'description ...lti-line text' == 'description ...lti-line text'
E         
E         - description 1 with multi-line text
E         + description 1
E         + with multi-line text

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_attributes_1_test_valid_input_multi_line.py:26: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_attributes_1_test_valid_input_multi_line.py::test_attributes
============================== 1 failed in 0.03s ===============================

"""