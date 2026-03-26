
from pytutils.lazy.simple_import import make_lazy
import sys
from types import ModuleType
from unittest.mock import patch
import pytest

@pytest.mark.parametrize("module_path", ["math"])
def test_valid_input(module_path):
    with patch('sys.modules', {'math': None}):
        make_lazy(module_path)
        assert module_path not in sys.modules, f"Expected {module_path} to be removed from sys.modules but it was found."

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

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input[math] ____________________________

module_path = 'math'

    @pytest.mark.parametrize("module_path", ["math"])
    def test_valid_input(module_path):
        with patch('sys.modules', {'math': None}):
            make_lazy(module_path)
>           assert module_path not in sys.modules, f"Expected {module_path} to be removed from sys.modules but it was found."
E           AssertionError: Expected math to be removed from sys.modules but it was found.
E           assert 'math' not in {'math': <pytutils.lazy.simple_import.make_lazy.<locals>.LazyModule object at 0x7f1f999a1a10>}
E            +  where {'math': <pytutils.lazy.simple_import.make_lazy.<locals>.LazyModule object at 0x7f1f999a1a10>} = sys.modules

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_valid_input.py::test_valid_input[math]
============================== 1 failed in 0.05s ===============================
"""