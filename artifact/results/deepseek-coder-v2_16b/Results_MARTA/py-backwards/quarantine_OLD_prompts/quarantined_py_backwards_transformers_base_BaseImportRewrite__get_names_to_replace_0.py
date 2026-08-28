
import ast
from unittest.mock import patch
from py_backwards.transformers.baseclass import BaseImportRewrite

def test_get_names_to_replace_with_rewrite():
    base_import = BaseImportRewrite()
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    node = ast.parse("from os import path").body[0]
    
    with patch('py_backwards.transformers.baseclass.BaseImportRewrite._get_matched_rewrite') as mock_get_matched_rewrite:
        mock_get_matched_rewrite.return_value = ('os', 'operating_system')
        
        replacements = list(base_import._get_names_to_replace(node))
        assert replacements == [('os.path', ('os', 'operating_system'))]

def test_get_names_to_replace_without_rewrite():
    base_import = BaseImportRewrite()
    base_import.rewrites = [('math', 'mathematics'), ('os', 'operating_system')]
    node = ast.parse("from unsupported import *").body[0]
    
    with patch('py_backwards.transformers.baseclass.BaseImportRewrite._get_matched_rewrite') as mock_get_matched_rewrite:
        mock_get_matched_rewrite.return_value = None
        
        replacements = list(base_import._get_names_to_replace(node))
        assert replacements == []

def test_get_names_to_replace_with_math():
    base_import = BaseImportRewrite()
    base_import.rewrites = [('math', 'mathematics')]
    node = ast.parse("from math import sqrt").body[0]
    
    with patch('py_backwards.transformers.baseclass.BaseImportRewrite._get_matched_rewrite') as mock_get_matched_rewrite:
        mock_get_matched_rewrite.return_value = ('math', 'mathematics')
        
        replacements = list(base_import._get_names_to_replace(node))
        assert replacements == [('math.sqrt', ('math', None))]

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
_ ERROR collecting test_py_backwards_transformers_base_BaseImportRewrite__get_names_to_replace_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite__get_names_to_replace_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite__get_names_to_replace_0.py:4: in <module>
    from py_backwards.transformers.baseclass import BaseImportRewrite
E   ModuleNotFoundError: No module named 'py_backwards.transformers.baseclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_base_BaseImportRewrite__get_names_to_replace_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""