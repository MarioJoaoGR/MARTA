
import pytest
from py_backwards.transformers.six_moves import MovedAttribute
import old_module as om
import new_module as nm

# Test minimal parameters provided (name, old_mod)
def test_minimal_parameters():
    moved_attr = MovedAttribute('old_attribute', om, nm)
    assert moved_attr.name == 'old_attribute'
    assert moved_attr.old_mod is om
    assert moved_attr.new_mod is nm
    assert moved_attr.new_attr == 'old_attribute'

# Test providing all parameters explicitly
def test_all_parameters_explicit():
    moved_attr = MovedAttribute('old_attribute', om, nm, 'new_attribute')
    assert moved_attr.name == 'old_attribute'
    assert moved_attr.old_mod is om
    assert moved_attr.new_mod is nm
    assert moved_attr.new_attr == 'new_attribute'

# Test only 'name' and 'old_mod' provided, defaulting to name for 'new_mod' and 'old_attr'
def test_default_parameters():
    moved_attr = MovedAttribute('old_attribute', om, nm, old_attr='old_attribute')
    assert moved_attr.name == 'old_attribute'
    assert moved_attr.old_mod is om
    assert moved_attr.new_mod is nm
    assert moved_attr.new_attr == 'old_attribute'

# Test only 'name' and 'old_mod' provided, defaulting to name for 'new_mod', 'old_attr', and 'new_attr'
def test_default_parameters_all():
    moved_attr = MovedAttribute('old_attribute', om, nm, new_attr='old_attribute')
    assert moved_attr.name == 'old_attribute'
    assert moved_attr.old_mod is om
    assert moved_attr.new_mod is nm
    assert moved_attr.new_attr == 'old_attribute'

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
_ ERROR collecting test_py_backwards_transformers_six_moves_MovedAttribute___init___0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_six_moves_MovedAttribute___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_six_moves_MovedAttribute___init___0.py:4: in <module>
    import old_module as om
E   ModuleNotFoundError: No module named 'old_module'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_six_moves_MovedAttribute___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""