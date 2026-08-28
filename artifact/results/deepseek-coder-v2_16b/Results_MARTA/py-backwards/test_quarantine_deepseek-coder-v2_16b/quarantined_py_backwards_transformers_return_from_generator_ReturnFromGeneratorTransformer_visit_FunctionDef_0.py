
import ast
import inspect
import pytest
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer_visit_FunctionDef_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def fn():
            yield 1
            return 5
    
        # Parse the function into an AST
>       tree = ast.parse(inspect.getsource(fn))

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer_visit_FunctionDef_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = '    def fn():\n        yield 1\n        return 5\n'
filename = '<unknown>', mode = 'exec'

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
E         File "<unknown>", line 1
E           def fn():
E       IndentationError: unexpected indent

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: IndentationError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       transformer = ReturnFromGeneratorTransformer()
E       TypeError: BaseNodeTransformer.__init__() missing 1 required positional argument: 'tree'

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer_visit_FunctionDef_0.py:39: TypeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        def fn():
            yield 1 # Syntax error here
    
        # Parse the function into an AST
>       tree = ast.parse(inspect.getsource(fn))

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer_visit_FunctionDef_0.py:48: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = '    def fn():\n        yield 1 # Syntax error here\n'
filename = '<unknown>', mode = 'exec'

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
E         File "<unknown>", line 1
E           def fn():
E       IndentationError: unexpected indent

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: IndentationError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer_visit_FunctionDef_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer_visit_FunctionDef_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer_visit_FunctionDef_0.py::test_invalid_input
============================== 3 failed in 0.13s ===============================
"""