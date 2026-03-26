
import pytest
from pytutils.pythree import ensure_decoded_text

def test_ensure_decoded_text():
    # Test with a Unicode string (Python 2 and 3 compatible)
    assert ensure_decoded_text(u"Hello, World!") == b'Hello, World!'

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

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_ensure_decoded_text ___________________________

    def test_ensure_decoded_text():
        # Test with a Unicode string (Python 2 and 3 compatible)
>       assert ensure_decoded_text(u"Hello, World!") == b'Hello, World!'
E       AssertionError: assert 'Hello, World!' == b'Hello, World!'
E        +  where 'Hello, World!' = ensure_decoded_text('Hello, World!')

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_0_test_edge_cases.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pythree_ensure_decoded_text_0_test_edge_cases.py::test_ensure_decoded_text
============================== 1 failed in 0.07s ===============================
"""