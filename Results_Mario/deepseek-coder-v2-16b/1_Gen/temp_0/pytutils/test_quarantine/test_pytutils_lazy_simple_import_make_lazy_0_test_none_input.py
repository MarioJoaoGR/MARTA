
from pytutils.lazy.simple_import import make_lazy
import sys
import pytest

def test_none_input():
    # Call make_lazy with None to ensure no module is imported yet
    make_lazy(None)
    
    # Check that the math module has not been imported by checking if it's in sys.modules
    assert 'math' not in sys.modules, f"The math module should not be imported yet."

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

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

>   ???
E   AssertionError: The math module should not be imported yet.
E   assert 'math' not in {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>, ...}
E    +  where {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>, ...} = sys.modules

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_none_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_none_input.py::test_none_input
============================== 1 failed in 0.05s ===============================
"""