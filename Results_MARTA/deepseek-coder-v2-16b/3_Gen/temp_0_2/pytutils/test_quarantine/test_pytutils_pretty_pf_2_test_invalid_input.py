
import pytest
from unittest.mock import patch, MagicMock
from pytutils.pretty import pf

def test_invalid_input():
    # Test when the argument is not a string or Python object (e.g., an integer)
    with patch('pytutils.pretty.__PP_LEXER_PYTHON', None):  # Mock lexer to be None for testing non-string input
        with patch('pytutils.pretty.__PP_FORMATTER', None):  # Mock formatter to be None for testing non-string input
            with pytest.raises(TypeError) as excinfo:
                pf(12345)  # Passing an integer, which is not a valid argument type
            assert "expected str, bytes or os.PathLike object, not int" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_pretty_pf_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test when the argument is not a string or Python object (e.g., an integer)
        with patch('pytutils.pretty.__PP_LEXER_PYTHON', None):  # Mock lexer to be None for testing non-string input
            with patch('pytutils.pretty.__PP_FORMATTER', None):  # Mock formatter to be None for testing non-string input
>               with pytest.raises(TypeError) as excinfo:
E               Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_pretty_pf_2_test_invalid_input.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pf_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""