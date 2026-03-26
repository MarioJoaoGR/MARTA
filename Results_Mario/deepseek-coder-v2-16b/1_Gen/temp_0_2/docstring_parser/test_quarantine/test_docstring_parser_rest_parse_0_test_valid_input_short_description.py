
import pytest
from docstring_parser.rest import parse, Docstring, DocstringStyle, DocstringParam, DocstringReturns

def test_valid_input_short_description():
    # Test when text is provided
    result = parse("This is a brief description.\n\nHere is a more detailed explanation.")
    assert isinstance(result, Docstring)
    assert result.style == DocstringStyle.REST
    assert result.short_description == 'This is a brief description.'
    assert result.long_description == 'Here is a more detailed explanation.'
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is True
    assert len(result.meta) == 0

    # Test when text contains parameter description
    result = parse(":param arg: This is a parameter.\n:type arg: int")
    assert isinstance(result, Docstring)
    assert result.style == DocstringStyle.REST
    assert result.short_description == 'arg'
    assert result.long_description == 'This is a parameter.'
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is False
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args == ['arg']
    assert result.meta[0].type_name == 'int'

    # Test when text contains return description
    result = parse(":returns: This function returns an integer.\n:rtype: int")
    assert isinstance(result, Docstring)
    assert result.style == DocstringStyle.REST
    assert result.short_description is None
    assert result.long_description == 'This function returns an integer.'
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is True
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringReturns)
    assert result.meta[0].args == ['returns']
    assert result.meta[0].type_name == 'int'

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

docstring_parser/Test4DT_tests/test_docstring_parser_rest_parse_0_test_valid_input_short_description.py F [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_short_description ______________________

    def test_valid_input_short_description():
        # Test when text is provided
        result = parse("This is a brief description.\n\nHere is a more detailed explanation.")
        assert isinstance(result, Docstring)
        assert result.style == DocstringStyle.REST
        assert result.short_description == 'This is a brief description.'
        assert result.long_description == 'Here is a more detailed explanation.'
        assert result.blank_after_short_description is True
>       assert result.blank_after_long_description is True
E       assert False is True
E        +  where False = <docstring_parser.common.Docstring object at 0x102f3b8b0>.blank_after_long_description

docstring_parser/Test4DT_tests/test_docstring_parser_rest_parse_0_test_valid_input_short_description.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_rest_parse_0_test_valid_input_short_description.py::test_valid_input_short_description
============================== 1 failed in 0.02s ===============================
"""