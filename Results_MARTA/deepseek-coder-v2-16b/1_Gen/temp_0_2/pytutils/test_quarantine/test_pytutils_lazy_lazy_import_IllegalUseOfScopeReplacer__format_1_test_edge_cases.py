
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer
import pytest

def test_edge_cases():
    # Test case 1: None as extra
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        IllegalUseOfScopeReplacer('test', 'This is a test message', extra=None)
    assert str(exc_info.value) == "ScopeReplacer object 'test' was used incorrectly: This is a test message."

    # Test case 2: Empty string as extra
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        IllegalUseOfScopeReplacer('test', 'This is another test message', extra='')
    assert str(exc_info.value) == "ScopeReplacer object 'test' was used incorrectly: This is another test message."

    # Test case 3: No extra provided
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        IllegalUseOfScopeReplacer('test', 'This is a third test message')
    assert str(exc_info.value) == "ScopeReplacer object 'test' was used incorrectly: This is a third test message."

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test case 1: None as extra
>       with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
E       Failed: DID NOT RAISE <class 'pytutils.lazy.lazy_import.IllegalUseOfScopeReplacer'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_1_test_edge_cases.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.05s ===============================
"""