
import ast
import pytest
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer

# Define a sample generator function for testing
def generator_fn():
    yield 1
    return 5

# Parse the function into an AST
tree = ast.parse(inspect.getsource(generator_fn))
root = tree.body[0]  # Assume it's a function definition

# Create an instance of the transformer
transformer = ReturnFromGeneratorTransformer()

def test_find_generator_returns():
    transformed_tree = transformer._find_generator_returns(root)
    assert len(transformed_tree) == 1
    stmt, ret_stmt = transformed_tree[0]
    assert isinstance(stmt, ast.FunctionDef)
    assert isinstance(ret_stmt, ast.Return)
    assert ret_stmt.value is not None
    assert ret_stmt.value.value == 5

def test_transform_function():
    transformed_tree = transformer.visit_FunctionDef(root)
    # Now the function 'generator_fn' should be transformed to:
    def generator_transformed():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    
    assert inspect.getsource(generator_transformed) == ast.unparse(transformed_tree)

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
_ ERROR collecting test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer__find_generator_returns_0.py _
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer__find_generator_returns_0.py:12: in <module>
    tree = ast.parse(inspect.getsource(generator_fn))
E   NameError: name 'inspect' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_ReturnFromGeneratorTransformer__find_generator_returns_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""