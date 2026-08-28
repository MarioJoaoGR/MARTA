
import pytest
from ast import Subscript, Name, Load, Tuple, Constant, BinOp, BitOr
from apimd.parser import Resolver



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Resolver_visit_Subscript_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_typing_union _______________________________

    def test_typing_union():
        resolver = Resolver(root='my_project', alias={'np': 'numpy', 'pd': 'pandas'}, self_ty='MyClass')
        subscript_node = Subscript(
            value=Name('Union', Load()),
            slice=Tuple([Name('int', Load()), Name('str', Load())], ctx=Load()),
            ctx=Load()
        )
        transformed_node = resolver.visit_Subscript(subscript_node)
>       assert isinstance(transformed_node, BinOp)
E       assert False
E        +  where False = isinstance(<ast.Subscript object at 0x7fb0d9db7fd0>, BinOp)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Resolver_visit_Subscript_0.py:14: AssertionError
_______________________________ test_empty_alias _______________________________

    def test_empty_alias():
        resolver = Resolver(root='my_project', alias={}, self_ty='MyClass')
        subscript_node = Subscript(
            value=Name('Union', Load()),
            slice=Tuple([Name('int', Load()), Name('str', Load())], ctx=Load()),
            ctx=Load()
        )
        transformed_node = resolver.visit_Subscript(subscript_node)
>       assert isinstance(transformed_node, BinOp)
E       assert False
E        +  where False = isinstance(<ast.Subscript object at 0x7fb0d9e4fbe0>, BinOp)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Resolver_visit_Subscript_0.py:25: AssertionError
____________________________ test_invalid_subscript ____________________________

    def test_invalid_subscript():
        resolver = Resolver(root='my_project', alias={'np': 'numpy', 'pd': 'pandas'}, self_ty='MyClass')
        subscript_node = Subscript(
            value=Name('Union', Load()),
            slice=Constant(123),
            ctx=Load()
        )
        transformed_node = resolver.visit_Subscript(subscript_node)
>       assert isinstance(transformed_node, Constant)
E       assert False
E        +  where False = isinstance(<ast.Subscript object at 0x7fb0d9db5570>, Constant)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Resolver_visit_Subscript_0.py:36: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Resolver_visit_Subscript_0.py::test_typing_union
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Resolver_visit_Subscript_0.py::test_empty_alias
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Resolver_visit_Subscript_0.py::test_invalid_subscript
============================== 3 failed in 0.06s ===============================
"""