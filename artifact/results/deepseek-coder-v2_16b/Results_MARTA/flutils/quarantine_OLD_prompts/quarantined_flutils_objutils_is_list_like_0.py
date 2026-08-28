
import pytest
from flutils.objutils import is_list_like
from collections.abc import Iterator, KeysView, ValuesView
from collections import deque, UserList, frozenset, list as pylist, set as pyset, tuple as pytuple

def test_is_list_like_true():
    assert is_list_like([1, 2, 3])
    assert is_list_like(reversed([1, 2, 4]))
    assert is_list_like('hello'.split())
    assert is_list_like(sorted('hello'))
    
    class CustomListLike:
        def __init__(self, items):
            self.items = items
        
        def __iter__(self):
            return iter(self.items)
    
    assert is_list_like(CustomListLike([1, 2, 3]))

def test_is_list_like_false():
    assert not is_list_like(None)
    assert not is_list_like(True)
    assert not is_list_like(b'hello')
    assert not is_list_like({'a': 1, 'b': 2})
    assert not is_list_like({1, 2, 3})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___________ ERROR collecting test_flutils_objutils_is_list_like_0.py ___________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_is_list_like_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_is_list_like_0.py:5: in <module>
    from collections import deque, UserList, frozenset, list as pylist, set as pyset, tuple as pytuple
E   ImportError: cannot import name 'frozenset' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_is_list_like_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""