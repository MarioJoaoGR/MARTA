
import ast
import pytest
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

# Test for transforming a list with starred unpacking into a sum of lists representation
@pytest.mark.parametrize("original, expected", [
    ([2, *range(10), 1], [2] + list(range(10)) + [1]),
    ([*range(5)], list(range(5))),
    ([1, *range(3, 6)], [1] + list(range(3, 6)))
])
def test_valid_list_transformation(original, expected):
    code = f"[{', '.join([str(e) for e in original])}]"
    tree = ast.parse(code)
    transformer = StarredUnpackingTransformer()
    transformed_tree = transformer.visit_Call(tree.body[0].value)
    
    assert isinstance(transformed_tree, ast.Call), "Expected a Call node"
    assert len(transformed_tree.args) == 1, "Expected one argument in the call"
    assert isinstance(transformed_tree.args[0], ast.Starred), "Expected starred expression"
    assert transformed_tree.args[0].value.elts == expected, "Transformed list does not match expected result"

# Test for transforming a print statement with starred unpacking into a print statement without starred unpacking
@pytest.mark.parametrize("original, expected", [
    ("print(*range(1), *range(3))", "print(*(list(range(1)) + list(range(3))))")
])
def test_valid_print_transformation(original, expected):
    tree = ast.parse(original)
    transformer = StarredUnpackingTransformer()
    transformed_call = transformer.visit_Call(tree.body[0].value)
    
    assert isinstance(transformed_call, ast.Call), "Expected a Call node"
    assert len(transformed_call.args) == 1, "Expected one argument in the call"
    assert isinstance(transformed_call.args[0], ast.Starred), "Expected starred expression"
    transformed_args = transformed_call.args[0].value.elts
    expected_args = [ast.Num(n=i) for i in range(1)] + [ast.Num(n=i) for i in range(3)]
    assert transformed_args == expected_args, "Transformed call arguments do not match expected result"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________ test_valid_list_transformation[original0-expected0] ______________

original = [2, 0, 1, 2, 3, 4, ...], expected = [2, 0, 1, 2, 3, 4, ...]

    @pytest.mark.parametrize("original, expected", [
        ([2, *range(10), 1], [2] + list(range(10)) + [1]),
        ([*range(5)], list(range(5))),
        ([1, *range(3, 6)], [1] + list(range(3, 6)))
    ])
    def test_valid_list_transformation(original, expected):
        code = f"[{', '.join([str(e) for e in original])}]"
        tree = ast.parse(code)
>       transformer = StarredUnpackingTransformer()
E       TypeError: BaseNodeTransformer.__init__() missing 1 required positional argument: 'tree'

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py:15: TypeError
_____________ test_valid_list_transformation[original1-expected1] ______________

original = [0, 1, 2, 3, 4], expected = [0, 1, 2, 3, 4]

    @pytest.mark.parametrize("original, expected", [
        ([2, *range(10), 1], [2] + list(range(10)) + [1]),
        ([*range(5)], list(range(5))),
        ([1, *range(3, 6)], [1] + list(range(3, 6)))
    ])
    def test_valid_list_transformation(original, expected):
        code = f"[{', '.join([str(e) for e in original])}]"
        tree = ast.parse(code)
>       transformer = StarredUnpackingTransformer()
E       TypeError: BaseNodeTransformer.__init__() missing 1 required positional argument: 'tree'

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py:15: TypeError
_____________ test_valid_list_transformation[original2-expected2] ______________

original = [1, 3, 4, 5], expected = [1, 3, 4, 5]

    @pytest.mark.parametrize("original, expected", [
        ([2, *range(10), 1], [2] + list(range(10)) + [1]),
        ([*range(5)], list(range(5))),
        ([1, *range(3, 6)], [1] + list(range(3, 6)))
    ])
    def test_valid_list_transformation(original, expected):
        code = f"[{', '.join([str(e) for e in original])}]"
        tree = ast.parse(code)
>       transformer = StarredUnpackingTransformer()
E       TypeError: BaseNodeTransformer.__init__() missing 1 required positional argument: 'tree'

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py:15: TypeError
_ test_valid_print_transformation[print(*range(1), *range(3))-print(*(list(range(1)) + list(range(3))))] _

original = 'print(*range(1), *range(3))'
expected = 'print(*(list(range(1)) + list(range(3))))'

    @pytest.mark.parametrize("original, expected", [
        ("print(*range(1), *range(3))", "print(*(list(range(1)) + list(range(3))))")
    ])
    def test_valid_print_transformation(original, expected):
        tree = ast.parse(original)
>       transformer = StarredUnpackingTransformer()
E       TypeError: BaseNodeTransformer.__init__() missing 1 required positional argument: 'tree'

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py:29: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py::test_valid_list_transformation[original0-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py::test_valid_list_transformation[original1-expected1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py::test_valid_list_transformation[original2-expected2]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_starred_unpacking_StarredUnpackingTransformer_visit_Call_0.py::test_valid_print_transformation[print(*range(1), *range(3))-print(*(list(range(1)) + list(range(3))))]
============================== 4 failed in 0.09s ===============================
"""