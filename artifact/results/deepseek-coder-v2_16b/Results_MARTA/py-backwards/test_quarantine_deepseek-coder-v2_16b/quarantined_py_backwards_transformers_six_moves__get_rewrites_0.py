
import pytest
from py_backwards.transformers.six_moves import _get_rewrites, prefixed_moves
from py_backwards.transformers.six_moves import MovedAttribute, MovedModule

# Define a sample prefixed_moves list for testing
prefixed_moves = [
    ('os', [MovedModule('os')]),
    ('sysconfig', [MovedModule('sysconfig')])
]

def test_get_rewrites_movedattribute():
    expected_output = [
        ('six.movesos.exists', 'os.path'),
        ('six.movessysconfig.get_paths', 'sysconfig.get_paths')
    ]
    
    result = list(_get_rewrites())
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_get_rewrites_movedmodule():
    expected_output = [
        ('six.movesos', 'os'),
        ('six.movessysconfig', 'sysconfig')
    ]
    
    result = list(_get_rewrites())
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_py_backwards_transformers_six_moves__get_rewrites_0.py _
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_six_moves__get_rewrites_0.py:8: in <module>
    ('os', [MovedModule('os')]),
E   TypeError: MovedModule.__init__() missing 1 required positional argument: 'old'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_six_moves__get_rewrites_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""