
import pytest
from py_backwards.utils.snippet import VariablesReplacer, Variable



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer__replace_module_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_replace_module ______________________________

    def test_replace_module():
        variables_dict = {
>           'x': Variable('uniqueVar1'),
            'y': Variable('uniqueVar2')
        }

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer__replace_module_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/typing.py:957: in __call__
    result = self.__origin__(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = typing.Union, args = ('uniqueVar1',), kwds = {}

    def __call__(self, *args, **kwds):
>       raise TypeError(f"Cannot instantiate {self!r}")
E       TypeError: Cannot instantiate typing.Union

/opt/conda/envs/test4py_env/lib/python3.10/typing.py:387: TypeError
__________________________ test_replace_field_or_node __________________________

    def test_replace_field_or_node():
        variables_dict = {
>           'x': Variable('uniqueVar1'),
            'y': Variable('uniqueVar2')
        }

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer__replace_module_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/typing.py:957: in __call__
    result = self.__origin__(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = typing.Union, args = ('uniqueVar1',), kwds = {}

    def __call__(self, *args, **kwds):
>       raise TypeError(f"Cannot instantiate {self!r}")
E       TypeError: Cannot instantiate typing.Union

/opt/conda/envs/test4py_env/lib/python3.10/typing.py:387: TypeError
_______________________________ test_replace_ast _______________________________

    def test_replace_ast():
        variables_dict = {
>           'x': Variable('uniqueVar1'),
            'y': Variable('uniqueVar2')
        }

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer__replace_module_0.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/typing.py:957: in __call__
    result = self.__origin__(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = typing.Union, args = ('uniqueVar1',), kwds = {}

    def __call__(self, *args, **kwds):
>       raise TypeError(f"Cannot instantiate {self!r}")
E       TypeError: Cannot instantiate typing.Union

/opt/conda/envs/test4py_env/lib/python3.10/typing.py:387: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer__replace_module_0.py::test_replace_module
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer__replace_module_0.py::test_replace_field_or_node
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer__replace_module_0.py::test_replace_ast
============================== 3 failed in 0.16s ===============================
"""