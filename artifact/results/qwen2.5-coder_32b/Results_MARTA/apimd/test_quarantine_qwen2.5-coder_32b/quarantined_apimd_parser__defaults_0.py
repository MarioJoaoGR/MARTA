
import pytest
from apimd.parser import _defaults
from ast import Constant



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser__defaults_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        args = [Constant(value='example|text'), None, Constant(value='example&text')]
        expected_output = ['example&#124;text', ' ', '<code>example&amp;text</code>']
>       assert list(_defaults(args)) == expected_output
E       assert ["<code>'exam...text'</code>"] == ['example&#12...;text</code>']
E         
E         At index 0 diff: "<code>'example&#124;text'</code>" != 'example&#124;text'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser__defaults_0.py:9: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        args = [None, None, Constant(value='value'), [], [None]]
        expected_output = [' ', ' ', '<code>value</code>', ' ', ' ']
>       assert list(_defaults(args)) == expected_output

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser__defaults_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:48: in _defaults
    yield from (code(unparse(a)) if a is not None else " " for a in args)
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:48: in <genexpr>
    yield from (code(unparse(a)) if a is not None else " " for a in args)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1681: in unparse
    return unparser.visit(ast_obj)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:815: in visit
    self.traverse(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:804: in traverse
    self.traverse(item)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:806: in traverse
    super().visit(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:418: in visit
    return visitor(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:422: in generic_visit
    for field, value in iter_fields(node):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = None

    def iter_fields(node):
        """
        Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
        that is present on *node*.
        """
>       for field in node._fields:
E       AttributeError: 'NoneType' object has no attribute '_fields'

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:260: AttributeError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        args = [123, 'string', {}, []]
        expected_output = [' ', ' ', ' ', ' ']
>       assert list(_defaults(args)) == expected_output

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser__defaults_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:48: in _defaults
    yield from (code(unparse(a)) if a is not None else " " for a in args)
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:48: in <genexpr>
    yield from (code(unparse(a)) if a is not None else " " for a in args)
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
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = 123

    def iter_fields(node):
        """
        Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
        that is present on *node*.
        """
>       for field in node._fields:
E       AttributeError: 'int' object has no attribute '_fields'

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:260: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser__defaults_0.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser__defaults_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser__defaults_0.py::test_invalid_inputs
============================== 3 failed in 0.24s ===============================
"""