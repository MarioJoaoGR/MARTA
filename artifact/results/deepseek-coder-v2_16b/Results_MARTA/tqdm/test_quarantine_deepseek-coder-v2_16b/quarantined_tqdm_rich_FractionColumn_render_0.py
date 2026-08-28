
import pytest
from fraction_column import FractionColumn, Task

def test_fraction_column_default():
    fc = FractionColumn()
    task = Task(completed=50, total=100)
    result = fc.render(task)
    assert result == "0.5/1"

def test_fraction_column_scaled():
    fc_scaled = FractionColumn(unit_scale=True, unit_divisor=100)
    task_large = Task(completed=2000, total=4000)
    result = fc_scaled.render(task_large)
    assert result == "0.5/1 K"

def test_fraction_column_no_scaling():
    fc_no_scale = FractionColumn(unit_scale=False, unit_divisor=1000)
    task = Task(completed=50, total=100)
    result = fc_no_scale.render(task)
    assert result == "0.5/1"

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
__________ ERROR collecting test_tqdm_rich_FractionColumn_render_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_rich_FractionColumn_render_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_rich_FractionColumn_render_0.py:3: in <module>
    from fraction_column import FractionColumn, Task
E   ModuleNotFoundError: No module named 'fraction_column'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_rich_FractionColumn_render_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""