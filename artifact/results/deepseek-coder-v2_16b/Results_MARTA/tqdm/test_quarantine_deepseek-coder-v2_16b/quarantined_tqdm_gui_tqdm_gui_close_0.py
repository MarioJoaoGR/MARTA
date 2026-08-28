
import pytest
from tqdm_gui import tqdm_gui

def test_tqdm_gui_default_usage():
    for i in tqdm_gui(range(100)):
        pass
    assert True, "Test should not raise any exceptions"

def test_tqdm_gui_with_custom_color():
    for i in tqdm_gui(range(100), colour='r'):
        pass
    assert True, "Test should not raise any exceptions"

def test_tqdm_gui_with_gui_mode():
    for i in tqdm_gui(range(100), gui=True):
        pass
    assert True, "Test should not raise any exceptions"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
______________ ERROR collecting test_tqdm_gui_tqdm_gui_close_0.py ______________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_close_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_close_0.py:3: in <module>
    from tqdm_gui import tqdm_gui
E   ModuleNotFoundError: No module named 'tqdm_gui'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_close_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""