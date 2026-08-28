
import pytest
from range_replacement import Range

def test_range_creation():
    r1 = Range(10)
    assert list(r1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    r2 = Range(1, 10 + 1)
    assert list(r2) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    r3 = Range(1, 11, 2)
    assert list(r3) == [1, 3, 5, 7, 9]

def test_range_indexing():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9

def test_range_invalid_creation():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________ ERROR collecting test_flutes_iterator_Range___iter___0.py ___________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___iter___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___iter___0.py:3: in <module>
    from range_replacement import Range
E   ModuleNotFoundError: No module named 'range_replacement'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___iter___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""