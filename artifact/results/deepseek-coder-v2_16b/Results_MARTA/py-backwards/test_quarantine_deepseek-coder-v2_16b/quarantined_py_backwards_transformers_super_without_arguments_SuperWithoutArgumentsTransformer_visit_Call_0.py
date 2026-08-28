
import ast
import pytest
from py_backwards.transformers.super_without_arguments import SuperWithoutArgumentsTransformer


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_super_without_arguments_SuperWithoutArgumentsTransformer_visit_Call_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_simple_method ________________________

    def test_valid_input_simple_method():
        sample_code = "class Example:\n    def method(self):\n        super().method()"
        sample_ast = ast.parse(sample_code)
        transformer = SuperWithoutArgumentsTransformer(sample_ast)
    
        for node in ast.walk(sample_ast):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'super':
>               transformed_node = transformer._replace_super_args(node)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_super_without_arguments_SuperWithoutArgumentsTransformer_visit_Call_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/transformers/super_without_arguments.py:20: in _replace_super_args
    func = get_closest_parent_of(self._tree, node, ast.FunctionDef)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:71: in get_closest_parent_of
    parent = get_parent(tree, parent)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7f11d5a5bee0>
key = <ast.Call object at 0x7f11d58758d0>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7f11d5884770; to 'Call' at 0x7f11d58758d0>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        transformer = SuperWithoutArgumentsTransformer(None)
        with pytest.raises(TypeError):
>           transformer._replace_super_args(None)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_super_without_arguments_SuperWithoutArgumentsTransformer_visit_Call_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/transformers/super_without_arguments.py:20: in _replace_super_args
    func = get_closest_parent_of(self._tree, node, ast.FunctionDef)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:71: in get_closest_parent_of
    parent = get_parent(tree, parent)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:18: in get_parent
    _build_parents(tree)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:10: in _build_parents
    for node in ast.walk(tree):
/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:251: in walk
    todo.extend(iter_child_nodes(node))
/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:209: in iter_child_nodes
    for name, field in iter_fields(node):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = None

    def iter_fields(node):
        """
        Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
        that is present on *node*.
        """
>       for field in node._fields:
E       AttributeError: 'NoneType' object has no attribute '_fields'

/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:197: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_super_without_arguments_SuperWithoutArgumentsTransformer_visit_Call_0.py::test_valid_input_simple_method
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_super_without_arguments_SuperWithoutArgumentsTransformer_visit_Call_0.py::test_edge_case_none
============================== 2 failed in 0.09s ===============================
"""