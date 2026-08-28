
import ast
import pytest
from py_backwards.utils.tree import _build_parents

# Define a dictionary to hold parent-child relationships
_parents = {}

@pytest.fixture(autouse=True)
def reset_parents():
    global _parents
    _parents = {}



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree__build_parents_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_build_parents_basic ___________________________

    def test_build_parents_basic():
        sample_ast = ast.parse("def example(): pass")
        _build_parents(sample_ast)
>       assert len(_parents) == 2, "Expected number of nodes to be 2"
E       AssertionError: Expected number of nodes to be 2
E       assert 0 == 2
E        +  where 0 = len({})

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree__build_parents_0.py:17: AssertionError
_________________________ test_build_parents_function __________________________

    def test_build_parents_function():
        sample_ast = ast.parse("def example() -> int: pass")
        _build_parents(sample_ast)
>       assert len(_parents) == 3, "Expected number of nodes to be 3"
E       AssertionError: Expected number of nodes to be 3
E       assert 0 == 3
E        +  where 0 = len({})

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree__build_parents_0.py:22: AssertionError
___________________________ test_build_parents_class ___________________________

    def test_build_parents_class():
        sample_ast = ast.parse("class Example: pass")
        _build_parents(sample_ast)
>       assert len(_parents) == 2, "Expected number of nodes to be 2"
E       AssertionError: Expected number of nodes to be 2
E       assert 0 == 2
E        +  where 0 = len({})

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree__build_parents_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree__build_parents_0.py::test_build_parents_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree__build_parents_0.py::test_build_parents_function
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree__build_parents_0.py::test_build_parents_class
============================== 3 failed in 0.06s ===============================
"""