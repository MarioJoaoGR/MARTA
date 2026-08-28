
import ast
from py_backwards.transformers.variables_annotations import VariablesAnnotationsTransformer
import pytest




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        tree = None
        transformer = VariablesAnnotationsTransformer()
        with pytest.raises(TypeError):
>           result = transformer.transform(tree)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/transformers/variables_annotations.py:23: in transform
    for node in find(tree, ast.AnnAssign):
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:43: in find
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
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        tree = 'not an AST'
        transformer = VariablesAnnotationsTransformer()
        with pytest.raises(TypeError):
>           result = transformer.transform(tree)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/transformers/variables_annotations.py:23: in transform
    for node in find(tree, ast.AnnAssign):
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:43: in find
    for node in ast.walk(tree):
/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:251: in walk
    todo.extend(iter_child_nodes(node))
/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:209: in iter_child_nodes
    for name, field in iter_fields(node):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = 'not an AST'

    def iter_fields(node):
        """
        Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
        that is present on *node*.
        """
>       for field in node._fields:
E       AttributeError: 'str' object has no attribute '_fields'

/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:197: AttributeError
____________________________ test_valid_annotation _____________________________

    def test_valid_annotation():
        source = """
        a: int = 10
        b: int
        """
>       tree = ast.parse(source)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = '\n    a: int = 10\n    b: int\n    ', filename = '<unknown>'
mode = 'exec'

    def parse(source, filename='<unknown>', mode='exec', *,
              type_comments=False, feature_version=None):
        """
        Parse the source into an AST node.
        Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
        Pass type_comments=True to get back type comments where the syntax allows.
        """
        flags = PyCF_ONLY_AST
        if type_comments:
            flags |= PyCF_TYPE_COMMENTS
        if isinstance(feature_version, tuple):
            major, minor = feature_version  # Should be a 2-tuple.
            assert major == 3
            feature_version = minor
        elif feature_version is None:
            feature_version = -1
        # Else it should be an int giving the minor version for 3.x.
>       return compile(source, filename, mode, flags,
                       _feature_version=feature_version)
E         File "<unknown>", line 2
E           a: int = 10
E       IndentationError: unexpected indent

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: IndentationError
_______________________________ test_no_changes ________________________________

    def test_no_changes():
        source = """
        a = 10
        b = None
        """
>       tree = ast.parse(source)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = '\n    a = 10\n    b = None\n    ', filename = '<unknown>'
mode = 'exec'

    def parse(source, filename='<unknown>', mode='exec', *,
              type_comments=False, feature_version=None):
        """
        Parse the source into an AST node.
        Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
        Pass type_comments=True to get back type comments where the syntax allows.
        """
        flags = PyCF_ONLY_AST
        if type_comments:
            flags |= PyCF_TYPE_COMMENTS
        if isinstance(feature_version, tuple):
            major, minor = feature_version  # Should be a 2-tuple.
            assert major == 3
            feature_version = minor
        elif feature_version is None:
            feature_version = -1
        # Else it should be an int giving the minor version for 3.x.
>       return compile(source, filename, mode, flags,
                       _feature_version=feature_version)
E         File "<unknown>", line 2
E           a = 10
E       IndentationError: unexpected indent

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: IndentationError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py::test_invalid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py::test_valid_annotation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_variables_annotations_VariablesAnnotationsTransformer_transform_0.py::test_no_changes
============================== 4 failed in 0.14s ===============================
"""