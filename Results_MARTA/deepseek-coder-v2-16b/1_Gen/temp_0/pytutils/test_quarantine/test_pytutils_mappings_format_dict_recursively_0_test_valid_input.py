
import pytest
from pytutils.mappings import format_dict_recursively

def test_valid_input():
    c = dict(num='{num} is {val}', num=10, val='a number')
    formatted_dict = format_dict_recursively(c)
    assert formatted_dict == {'num': '10 is a number', 'val': 'a number'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_valid_input.py _
/usr/local/lib/python3.11/site-packages/_pytest/python.py:493: in importtestmodule
    mod = import_path(
/usr/local/lib/python3.11/site-packages/_pytest/pathlib.py:582: in import_path
    importlib.import_module(module_name)
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
<frozen importlib._bootstrap>:1176: in _find_and_load
    ???
<frozen importlib._bootstrap>:1147: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:690: in _load_unlocked
    ???
/usr/local/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:165: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
/usr/local/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:347: in _rewrite_test
    co = compile(tree, strfn, "exec", dont_inherit=True)
E     File "/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_valid_input.py", line 6
E       c = dict(num='{num} is {val}', num=10, val='a number')
E                                      ^^^^^^
E   SyntaxError: keyword argument repeated: num
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""