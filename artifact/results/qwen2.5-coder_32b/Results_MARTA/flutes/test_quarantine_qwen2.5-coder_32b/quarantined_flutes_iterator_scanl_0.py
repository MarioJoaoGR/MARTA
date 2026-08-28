
import pytest
from flutes.iterator import scanl
from operator import add, mul, max as op_max

def test_cumulative_sum():
    result = list(scanl(add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]

def test_cumulative_product():
    result = list(scanl(mul, [1, 2, 3, 4]))
    assert result == [1, 2, 6, 24]

def test_cumulative_max():
    result = list(scanl(op_max, [3, 1, 4, 1, 5, 9, 2, 6, 5]))
    assert result == [3, 3, 4, 4, 5, 9, 9, 9, 9]

def test_empty_iterable():
    with pytest.raises(RuntimeError):
        list(scanl(lambda x, y: x + y, []))

def test_single_element_iterable():
    result = list(scanl(add, [1]))
    assert result == [1]

def test_cumulative_subtraction():
    result = list(scanl(lambda x, y: x - y, [10, 2, 3]))
    assert result == [10, 8, 5]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______________ ERROR collecting test_flutes_iterator_scanl_0.py _______________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanl_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanl_0.py:4: in <module>
    from operator import add, mul, max as op_max
E   ImportError: cannot import name 'max' from 'operator' (/opt/conda/envs/test4py_env/lib/python3.10/operator.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanl_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""