
import ast
from unittest.mock import patch, MagicMock
import pytest
from py_backwards.transformers.baseclass import BaseImportRewrite

# Test case for visit_Import when a match is found in rewrites list
def test_visit_Import_with_match():
    base_import = BaseImportRewrite()
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    
    module_code = "from math import sqrt"
    parsed_module = ast.parse(module_code)
    rewritten_node = base_import.visit_Import(parsed_module.body[0].value)
    
    assert isinstance(rewritten_node, ast.Try), "Expected a Try node after match found in rewrites"
    assert len(rewritten_node.body) == 2, "Expected two import statements inside the try block"
    assert all(isinstance(stmt, ast.Import) for stmt in rewritten_node.body), "Both statements should be Import nodes"
    
    # Check if one of the imports is from 'mathematics' instead of 'math'
    matched = False
    for stmt in rewritten_node.body:
        if isinstance(stmt, ast.Import) and stmt.names[0].name == 'mathematics':
            matched = True
            break
    
    assert matched, "Expected one import to be from 'mathematics' instead of 'math'"

# Test case for visit_Import when no match is found in rewrites list
def test_visit_Import_no_match():
    base_import = BaseImportRewrite()
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    
    module_code = "from other_module import function"
    parsed_module = ast.parse(module_code)
    rewritten_node = base_import.visit_Import(parsed_module.body[0].value)
    
    assert isinstance(rewritten_node, ast.Import), "Expected an original Import node when no match is found"
    assert rewritten_node.names[0].name == 'other_module', "Original import should remain unchanged"

# Test case for visit_Import with mocked rewrites list to simulate module not found error
@patch('py_backwards.transformers.baseclass.BaseImportRewrite.rewrites', new=[])
def test_visit_Import_no_rewrites():
    base_import = BaseImportRewrite()
    module_code = "from math import sqrt"
    parsed_module = ast.parse(module_code)
    rewritten_node = base_import.visit_Import(parsed_module.body[0].value)
    
    assert isinstance(rewritten_node, ast.Import), "Expected an original Import node when rewrites list is empty"
    assert rewritten_node.names[0].name == 'math', "Original import should remain unchanged even with no rewrites"

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
_ ERROR collecting test_py_backwards_transformers_base_BaseImportRewrite_visit_Import_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite_visit_Import_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite_visit_Import_0.py:5: in <module>
    from py_backwards.transformers.baseclass import BaseImportRewrite
E   ModuleNotFoundError: No module named 'py_backwards.transformers.baseclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite_visit_Import_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""