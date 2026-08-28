
import pytest
from unittest.mock import patch, MagicMock
from pytutils.lazy.ImportProcessor import ImportProcessor
from pytutils.lazy.lazy_import import lazy_import

# Test 1: Initialize ImportProcessor with default ImportReplacer
def test_initialize_with_default():
    processor = ImportProcessor()
    assert isinstance(processor._lazy_import_class, type)
    assert issubclass(processor._lazy_import_class, ImportReplacer)

# Test 2: Initialize ImportProcessor with custom lazy import replacement logic
def test_initialize_with_custom():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    assert isinstance(processor._lazy_import_class, CustomLazyImport)

# Test 3: Process text with lazy imports
def test_process_text():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    text = "from math import sqrt"
    processed_text = processor.process_text(text)
    assert processed_text == "lazy_import('math').sqrt"

# Test 4: Build a map of imports from text
def test_build_map():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    text = """
    from math import sqrt
    from os import path as op
    import sys
    """
    processor._build_map(text)
    assert 'math' in processor.imports
    assert 'os' in processor.imports
    assert 'sys' in processor.imports

# Test 5: Convert imports in a scope
def test_convert_imports():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    scope = {}
    processor.imports = {
        'math': (['math'], None, {'sqrt':(['math'], 'sqrt', {})})
    }
    processor._convert_imports(scope)
    assert 'lazy_import' in scope
    assert hasattr(scope['lazy_import'], 'math')
    assert hasattr(scope['lazy_import'].math, 'sqrt')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0.py:4: in <module>
    from pytutils.lazy.ImportProcessor import ImportProcessor
E   ModuleNotFoundError: No module named 'pytutils.lazy.ImportProcessor'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""