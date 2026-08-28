
import pytest
from py_backwards.utils.helpers import get_source
from inspect import getsource
import re

def example_function():
    """Example docstring."""
    pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_get_source_1.py F [100%]

=================================== FAILURES ===================================
____________________ test_get_source_with_example_function _____________________

    def test_get_source_with_example_function():
        source_code = getsource(example_function).strip()
>       assert get_source(example_function) == source_code
E       assert 'def example_..."\n    pass\n' == 'def example_..."""\n    pass'
E         
E         Skipping 50 identical leading characters in diff, use -v to show
E           ""
E         -     pass
E         +     pass
E         ?         +

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_get_source_1.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_get_source_1.py::test_get_source_with_example_function
============================== 1 failed in 0.07s ===============================
"""