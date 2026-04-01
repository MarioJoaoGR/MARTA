
import ast
import pytest
from docstring_parser.attrdoc import ast_get_attribute, ast_unparse

@pytest.mark.parametrize("node", [
    pytest.param(ast.Assign(targets=[ast.Name(id='test_attr')], value=None), id="assign_no_value"),
    pytest.param(ast.AnnAssign(target=ast.Name(id='test_attr'), annotation=ast.Constant(value='int'), value=None), id="ann_assign")
])
def test_valid_input(node):
    result = ast_get_attribute(node)
    if isinstance(node, ast.Assign):
        assert result == ('test_attr', None, None)
    elif isinstance(node, ast.AnnAssign):
        assert result == ('test_attr', 'int', None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_valid_input.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input[ann_assign] _________________________

node = <ast.AnnAssign object at 0x1024b3f10>

    @pytest.mark.parametrize("node", [
        pytest.param(ast.Assign(targets=[ast.Name(id='test_attr')], value=None), id="assign_no_value"),
        pytest.param(ast.AnnAssign(target=ast.Name(id='test_attr'), annotation=ast.Constant(value='int'), value=None), id="ann_assign")
    ])
    def test_valid_input(node):
        result = ast_get_attribute(node)
        if isinstance(node, ast.Assign):
            assert result == ('test_attr', None, None)
        elif isinstance(node, ast.AnnAssign):
>           assert result == ('test_attr', 'int', None)
E           assert ('test_attr', "'int'", None) == ('test_attr', 'int', None)
E             
E             At index 1 diff: "'int'" != 'int'
E             Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_valid_input.py::test_valid_input[ann_assign]
========================= 1 failed, 1 passed in 0.04s ==========================
"""