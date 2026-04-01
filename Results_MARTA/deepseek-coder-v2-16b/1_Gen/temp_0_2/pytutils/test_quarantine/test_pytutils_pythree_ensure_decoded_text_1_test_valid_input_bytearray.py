
import pytest
from pytutils.pythree import ensure_decoded_text
import six

def test_valid_input_bytearray():
    s = bytearray(b'Hello')
    assert ensure_decoded_text(s) == b'Hello'

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

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_1_test_valid_input_bytearray.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_input_bytearray __________________________

    def test_valid_input_bytearray():
        s = bytearray(b'Hello')
>       assert ensure_decoded_text(s) == b'Hello'
E       AssertionError: assert 'Hello' == b'Hello'
E        +  where 'Hello' = ensure_decoded_text(bytearray(b'Hello'))

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_1_test_valid_input_bytearray.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_1_test_valid_input_bytearray.py::test_valid_input_bytearray
============================== 1 failed in 0.05s ===============================
"""