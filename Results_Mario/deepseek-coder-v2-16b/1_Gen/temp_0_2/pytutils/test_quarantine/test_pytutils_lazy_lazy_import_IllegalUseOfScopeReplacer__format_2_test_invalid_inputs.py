
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer
import pytest

def test_invalid_inputs():
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        try:
            scope_replacer = IllegalUseOfScopeReplacer(123, 'error message', 456)
        except Exception as e:
            pass
    assert str(exc_info.value) == "ScopeReplacer object 123 was used incorrectly: error message: 456"

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
E       Failed: DID NOT RAISE <class 'pytutils.lazy.lazy_import.IllegalUseOfScopeReplacer'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_2_test_invalid_inputs.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""