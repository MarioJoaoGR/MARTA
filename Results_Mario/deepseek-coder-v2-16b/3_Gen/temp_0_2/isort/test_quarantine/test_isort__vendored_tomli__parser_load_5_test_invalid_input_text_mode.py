
import pytest
from io import StringIO
from isort._vendored.tomli._parser import load
from typing import Dict, Any, IO

def test_invalid_input_text_mode():
    # Create a mock file object with invalid text content
    fp = StringIO("invalid_content")
    
    # Call the load function and expect an exception due to malformed TOML
    with pytest.raises(Exception) as excinfo:
        load(fp)
    
    # Assert that the exception message contains the expected keyword 'parse_float'
    assert "Unexpected" in str(excinfo.value)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_5_test_invalid_input_text_mode.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_input_text_mode _________________________

    def test_invalid_input_text_mode():
        # Create a mock file object with invalid text content
        fp = StringIO("invalid_content")
    
        # Call the load function and expect an exception due to malformed TOML
        with pytest.raises(Exception) as excinfo:
            load(fp)
    
        # Assert that the exception message contains the expected keyword 'parse_float'
>       assert "Unexpected" in str(excinfo.value)
E       assert 'Unexpected' in 'Expected "=" after a key in a key/value pair (at end of document)'
E        +  where 'Expected "=" after a key in a key/value pair (at end of document)' = str(TOMLDecodeError('Expected "=" after a key in a key/value pair (at end of document)'))
E        +    where TOMLDecodeError('Expected "=" after a key in a key/value pair (at end of document)') = <ExceptionInfo TOMLDecodeError('Expected "=" after a key in a key/value pair (at end of document)') tblen=5>.value

isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_5_test_invalid_input_text_mode.py:16: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_isort__vendored_tomli__parser_load_5_test_invalid_input_text_mode.py::test_invalid_input_text_mode
  /projects/F202407648IACDCF2/mario/isort/isort/_vendored/tomli/_parser.py:61: DeprecationWarning: Text file object support is deprecated in favor of binary file objects. Use `open("foo.toml", "rb")` to open the file in binary mode.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_5_test_invalid_input_text_mode.py::test_invalid_input_text_mode
========================= 1 failed, 1 warning in 0.13s =========================
"""