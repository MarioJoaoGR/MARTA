
import pytest
from apimd.parser import Parser
from ast import arg



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_ann_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_happy_path_instance_method ________________________

    def test_happy_path_instance_method():
        p = Parser()
        args = [
            arg(arg='self', annotation=None),
            arg(arg='param1', annotation=arg(annotation='int')),
            arg(arg='param2', annotation=arg(annotation='str'))
        ]
        root = 'my_project'
        has_self = True
        cls_method = False
    
>       annotations = list(p.func_ann(root=root, args=args, has_self=has_self, cls_method=cls_method))

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_ann_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:509: in func_ann
    yield self.resolve(root, a.annotation, self_ty)
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:516: in resolve
    return unparse(r.generic_visit(r.visit(node)))
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1681: in unparse
    return unparser.visit(ast_obj)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:815: in visit
    self.traverse(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:806: in traverse
    super().visit(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:418: in visit
    return visitor(node)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ast._Unparser object at 0x7f3b0e2c37f0>
node = <ast.arg object at 0x7f3b0e2c1ff0>

    def visit_arg(self, node):
>       self.write(node.arg)
E       AttributeError: 'arg' object has no attribute 'arg'

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1508: AttributeError
_________________________ test_happy_path_class_method _________________________

    def test_happy_path_class_method():
        p = Parser()
        args = [
            arg(arg='self', annotation=None),
            arg(arg='param1', annotation=arg(annotation='int')),
            arg(arg='param2', annotation=arg(annotation='str'))
        ]
        root = 'my_project'
        has_self = True
        cls_method = True
    
>       annotations = list(p.func_ann(root=root, args=args, has_self=has_self, cls_method=cls_method))

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_ann_0.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:509: in func_ann
    yield self.resolve(root, a.annotation, self_ty)
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:516: in resolve
    return unparse(r.generic_visit(r.visit(node)))
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1681: in unparse
    return unparser.visit(ast_obj)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:815: in visit
    self.traverse(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:806: in traverse
    super().visit(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:418: in visit
    return visitor(node)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ast._Unparser object at 0x7f3b0e18bee0>
node = <ast.arg object at 0x7f3b0fab0370>

    def visit_arg(self, node):
>       self.write(node.arg)
E       AttributeError: 'arg' object has no attribute 'arg'

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1508: AttributeError
________________________ test_happy_path_static_method _________________________

    def test_happy_path_static_method():
        p = Parser()
        args = [
            arg(arg='param1', annotation=arg(annotation='int')),
            arg(arg='param2', annotation=arg(annotation='str'))
        ]
        root = 'my_project'
        has_self = False
        cls_method = False
    
>       annotations = list(p.func_ann(root=root, args=args, has_self=has_self, cls_method=cls_method))

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_ann_0.py:46: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:509: in func_ann
    yield self.resolve(root, a.annotation, self_ty)
/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:516: in resolve
    return unparse(r.generic_visit(r.visit(node)))
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1681: in unparse
    return unparser.visit(ast_obj)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:815: in visit
    self.traverse(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:806: in traverse
    super().visit(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:418: in visit
    return visitor(node)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ast._Unparser object at 0x7f3b0df538e0>
node = <ast.arg object at 0x7f3b0df53b80>

    def visit_arg(self, node):
>       self.write(node.arg)
E       AttributeError: 'arg' object has no attribute 'arg'

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:1508: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_ann_0.py::test_happy_path_instance_method
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_ann_0.py::test_happy_path_class_method
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_func_ann_0.py::test_happy_path_static_method
============================== 3 failed in 0.28s ===============================
"""