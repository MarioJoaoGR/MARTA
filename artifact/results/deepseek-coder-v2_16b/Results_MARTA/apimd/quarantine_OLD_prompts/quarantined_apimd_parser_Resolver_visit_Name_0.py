
import pytest
from ast import Name, Load, Call
from apimd.parser import Resolver
from unittest.mock import patch



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Name_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_resolve_aliased_name ___________________________

    def test_resolve_aliased_name():
        resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a"})
        node = Name("a", Load())
        resolved_node = resolver.visit_Name(node)
        assert isinstance(resolved_node, Name)
>       assert resolved_node.id == "mypackage.module_a"
E       AssertionError: assert 'a' == 'mypackage.module_a'
E         
E         - mypackage.module_a
E         + a

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Name_0.py:12: AssertionError
_____________________________ test_resolve_typevar _____________________________

    def test_resolve_typevar():
        with patch('apimd.parser._m', return_value='typing.TypeVar'):
            resolver = Resolver(root="mypackage", alias={"TypeVar": "typing.TypeVar"})
            node = Call(Name("TypeVar", Load()), args=[], keywords=[])
>           resolved_node = resolver.visit_Name(node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Name_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <apimd.parser.Resolver object at 0x7fd0c972e380>
node = <ast.Call object at 0x7fd0c972e0b0>

    def visit_Name(self, node: Name) -> AST:
        """Replace global names with its expression recursively."""
>       if node.id == self.self_ty:
E       AttributeError: 'Call' object has no attribute 'id'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:221: AttributeError
____________________________ test_resolve_self_type ____________________________

    def test_resolve_self_type():
        resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a"}, self_ty="MyClass")
        node = Name("Self", Load())
        resolved_node = resolver.visit_Name(node)
        assert isinstance(resolved_node, Name)
>       assert resolved_node.id == "MyClass"
E       AssertionError: assert 'Self' == 'MyClass'
E         
E         - MyClass
E         + Self

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Name_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Name_0.py::test_resolve_aliased_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Name_0.py::test_resolve_typevar
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Name_0.py::test_resolve_self_type
============================== 3 failed in 0.07s ===============================
"""