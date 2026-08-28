
import pytest
import ast
from py_backwards.transformers.baseclass import BaseImportRewrite

# Test data for names to replace
NAMES_TO_REPLACE = {
    'math': ('old_module', 'new_module'),
    'os': ('another_module', 'replacement_module')
}

@pytest.fixture
def base_import():
    return BaseImportRewrite()

@pytest.fixture(params=[
    "from math import sqrt",
    "from os import path"
])
def module_code(request):
    return request.param

def test_replace_import_from_names(base_import, module_code):
    parsed_module = ast.parse(module_code)
    node = parsed_module.body[0].value  # Assuming the first import in the body is what we want to modify
    
    rewritten_node = base_import._replace_import_from_names(node, NAMES_TO_REPLACE)
    
    assert isinstance(rewritten_node, ast.Try), "Expected a Try node"
    for alias in node.names:
        if alias.name == 'math':
            assert rewritten_node.body[0].value.names[0].module == 'new_module', "Module name not replaced correctly"
        elif alias.name == 'os':
            assert rewritten_node.body[0].value.names[0].module == 'replacement_module', "Module name not replaced correctly"

def test_replace_import_from_names_no_match(base_import):
    module_code = "from random import randint"
    parsed_module = ast.parse(module_code)
    node = parsed_module.body[0].value  # Assuming the first import in the body is what we want to modify
    
    rewritten_node = base_import._replace_import_from_names(node, NAMES_TO_REPLACE)
    
    assert isinstance(rewritten_node, ast.Try), "Expected a Try node"
    for alias in node.names:
        assert alias.name == 'randint', "No match should not change the original import statement"

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
_ ERROR collecting test_py_backwards_transformers_base_BaseImportRewrite__replace_import_from_names_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite__replace_import_from_names_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite__replace_import_from_names_0.py:4: in <module>
    from py_backwards.transformers.baseclass import BaseImportRewrite
E   ModuleNotFoundError: No module named 'py_backwards.transformers.baseclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite__replace_import_from_names_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""