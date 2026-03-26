
import pytest
from isort._vendored.tomli._parser import parse_array, skip_comments_and_array_ws

def test_error_case():
    with pytest.raises(ValueError) as excinfo:
        src = "["
        pos = 0
        parse_float = float
        final_pos, parsed_array = parse_array(src, pos, parse_float)
    assert str(excinfo.value) == "Unclosed array"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with pytest.raises(ValueError) as excinfo:
            src = "["
            pos = 0
            parse_float = float
            final_pos, parsed_array = parse_array(src, pos, parse_float)
>       assert str(excinfo.value) == "Unclosed array"
E       AssertionError: assert 'Invalid valu... of document)' == 'Unclosed array'
E         
E         - Unclosed array
E         + Invalid value (at end of document)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_error_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_0_test_error_case.py::test_error_case
============================== 1 failed in 0.13s ===============================
"""