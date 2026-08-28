
import pytest
from pytutils.lazy import lazy_import

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_disallow_proxying_1.py F [100%]

=================================== FAILURES ===================================
____________________________ test_disallow_proxying ____________________________

    def test_disallow_proxying():
        """Test that disallowing proxying works correctly."""
        from pytutils.lazy.lazy_import import ScopeReplacer
    
        # Save the original value of _should_proxy to restore it after the test
        original_value = ScopeReplacer._should_proxy
    
        try:
            lazy_import.disallow_proxying()
    
            # Check that _should_proxy is now False
            assert not ScopeReplacer._should_proxy, "Expected _should_proxy to be set to False"
    
            # Attempt to import a module and ensure it doesn't proxy
            with pytest.raises(AttributeError):
>               from some_non_existent_module import SomeClass  # This should raise an AttributeError
E               ModuleNotFoundError: No module named 'some_non_existent_module'

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_disallow_proxying_1.py:20: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_disallow_proxying_1.py::test_disallow_proxying
============================== 1 failed in 0.05s ===============================
"""