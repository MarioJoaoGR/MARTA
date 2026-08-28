
import ast
import pytest
from py_backwards.transformers.base import BaseNodeTransformer


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseNodeTransformer___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        from py_backwards.transformers.base import BaseNodeTransformer
        tree = ast.parse('def greet(name): print(f"Hello, {name}!")')
        transformer = BaseNodeTransformer(tree)
        assert isinstance(transformer._tree, ast.AST), "Expected AST but got NoneType"
>       assert not hasattr(transformer, "_tree_changed"), "Tree should not be changed by default initialization"
E       AssertionError: Tree should not be changed by default initialization
E       assert not True
E        +  where True = hasattr(<py_backwards.transformers.base.BaseNodeTransformer object at 0x7f518404d030>, '_tree_changed')

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseNodeTransformer___init___0.py:11: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        from py_backwards.transformers.base import BaseNodeTransformer
        transformer = BaseNodeTransformer(None)
        assert transformer._tree is None, "Expected tree to be None but got an AST instance"
>       assert not hasattr(transformer, "_tree_changed"), "Tree should not be changed by default initialization when input is None"
E       AssertionError: Tree should not be changed by default initialization when input is None
E       assert not True
E        +  where True = hasattr(<py_backwards.transformers.base.BaseNodeTransformer object at 0x7f51849d6f80>, '_tree_changed')

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseNodeTransformer___init___0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseNodeTransformer___init___0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseNodeTransformer___init___0.py::test_edge_case
============================== 2 failed in 0.07s ===============================
"""