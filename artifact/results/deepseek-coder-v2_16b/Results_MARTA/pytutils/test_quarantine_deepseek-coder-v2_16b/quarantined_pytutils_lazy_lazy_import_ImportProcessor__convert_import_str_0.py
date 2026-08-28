
import pytest
from pytutils.lazy.lazy_import import ImportReplacer
from import_processor import ImportProcessor

# Test 1: Default Usage of ImportProcessor
def test_default_usage():
    processor = ImportProcessor()
    text = "from math import sqrt"
    processed_text = processor._convert_import_str(text)
    assert isinstance(processed_text, dict), f"Expected a dictionary but got {type(processed_text)}"
    assert 'sqrt' in processor.imports, "Expected 'sqrt' to be in imports"

# Test 2: Custom Lazy Import Replacement Logic
def test_custom_lazy_import():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    text = "from math import sqrt"
    processed_text = processor._convert_import_str(text)
    assert isinstance(processed_text, dict), f"Expected a dictionary but got {type(processed_text)}"
    assert 'sqrt' in processor.imports, "Expected 'sqrt' to be in imports"

# Test 3: Processing Text with Import Statements
def test_process_import_statements():
    processor = ImportProcessor()
    try:
        text = "import foo, foo.bar, foo.bar.baz as bing"
        processed_text = processor._convert_import_str(text)
        assert isinstance(processed_text, dict), f"Expected a dictionary but got {type(processed_text)}"
        assert 'foo' in processor.imports, "Expected 'foo' to be in imports"
        assert 'bar' in processor.imports['foo'], "Expected 'bar' to be in the sub-imports of 'foo'"
        assert 'baz' in processor.imports['foo']['bar'], "Expected 'baz' to be in the sub-imports of 'foo.bar'"
    except ValueError as e:
        pytest.fail(f"Unexpected ValueError: {e}")

# Test 4: Handling Import Statements with Spaces and Aliases
def test_handle_spaces_and_aliases():
    processor = ImportProcessor()
    try:
        text = "from math import sqrt, cos"
        processed_text = processor._convert_import_str(text)
        assert isinstance(processed_text, dict), f"Expected a dictionary but got {type(processed_text)}"
        assert 'sqrt' in processor.imports, "Expected 'sqrt' to be in imports"
        assert 'cos' in processor.imports, "Expected 'cos' to be in imports"
    except ValueError as e:
        pytest.fail(f"Unexpected ValueError: {e}")

# Test 5: Using ImportProcessor with a Specific Module Path
def test_specific_module_path():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    text = "from math import sqrt"
    processed_text = processor._convert_import_str(text)
    assert isinstance(processed_text, dict), f"Expected a dictionary but got {type(processed_text)}"
    assert 'sqrt' in processor.imports, "Expected 'sqrt' to be in imports"

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
_ ERROR collecting test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_0.py:4: in <module>
    from import_processor import ImportProcessor
E   ModuleNotFoundError: No module named 'import_processor'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""