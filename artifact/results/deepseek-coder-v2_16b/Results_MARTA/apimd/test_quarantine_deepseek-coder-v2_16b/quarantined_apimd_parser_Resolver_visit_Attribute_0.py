
import pytest
from apimd.parser import Resolver
from astroid.nodes import Attribute, Name, Load

# Test to check if visit_Attribute correctly removes typing.* prefix
def test_visit_attribute():
    resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a"})
    node = Attribute(Name('typing', Load()), Name('List', Load()))
    expected_node = Name('List', Load())
    
    result_node = resolver.visit_Attribute(node)
    
    assert isinstance(result_node, Name)
    assert result_node.name == 'List'

# Test to check if visit_Attribute returns the node unchanged if it is not an Attribute of typing.*
def test_visit_attribute_unchanged():
    resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a"})
    node = Name('some_other_name', Load())
    
    result_node = resolver.visit_Attribute(node)
    
    assert isinstance(result_node, Name)
    assert result_node.name == 'some_other_name'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_apimd_parser_Resolver_visit_Attribute_0.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Attribute_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Attribute_0.py:4: in <module>
    from astroid.nodes import Attribute, Name, Load
E   ImportError: cannot import name 'Load' from 'astroid.nodes' (/data/pydeps/marta/astroid/nodes/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Attribute_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""