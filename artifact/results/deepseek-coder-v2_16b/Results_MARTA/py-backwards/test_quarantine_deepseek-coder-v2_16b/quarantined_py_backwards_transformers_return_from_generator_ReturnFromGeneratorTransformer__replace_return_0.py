
import ast
import pytest
from py_backwards.transformers import ReturnFromGeneratorTransformer

# Define a sample generator function with return statement
def gen_fn():
    yield 1
    return 5

# Parse the function into an AST
tree = ast.parse(ast.unparse(gen_fn))
root = tree.body[0]  # Assume it's a function definition

# Create an instance of the transformer
transformer = ReturnFromGeneratorTransformer()

# Visit the FunctionDef node to replace return with StopIteration
transformed_tree = transformer._replace_return(root)

def test_transform_generator_function():
    # Define expected transformed function source code
    expected_source = """
def gen_fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc
"""
    
    # Parse the expected source into an AST
    expected_tree = ast.parse(expected_source)
    expected_root = expected_tree.body[0]
    
    # Compare the transformed tree with the expected tree
    assert ast.unparse(transformed_tree) == ast.unparse(expected_root)

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
_ ERROR collecting test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer__replace_return_0.py _
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer__replace_return_0.py:12: in <module>
    tree = ast.parse(ast.unparse(gen_fn))
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1681: in unparse
    return unparser.visit(ast_obj)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:815: in visit
    self.traverse(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:806: in traverse
    super().visit(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:418: in visit
    return visitor(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:422: in generic_visit
    for field, value in iter_fields(node):
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:260: in iter_fields
    for field in node._fields:
E   AttributeError: 'function' object has no attribute '_fields'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer__replace_return_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.19s ===============================
"""