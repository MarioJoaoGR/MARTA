
import pytest
from pytutils.lazy import ImportReplacer
from pytutils.errors import ImportNameCollision

class TestImportProcessor:
    """
    This class contains tests for the `ImportProcessor` class.
    """
    
    def test_default_import_replacer(self):
        """
        Test that the default import replacer is used when no custom class is provided.
        """
        processor = ImportProcessor()
        text = "from math import sqrt"
        processed_text = processor._convert_from_str(text)
        assert processed_text == 'lazy_import(\'math\').sqrt', f"Expected 'lazy_import(\'math\').sqrt' but got {processed_text}"
    
    def test_custom_import_replacer(self):
        """
        Test that a custom import replacer is used when provided.
        """
        class CustomLazyImport(ImportReplacer):
            def replace_import(self, module_name):
                return f"lazy_import('{module_name}')"
        
        processor = ImportProcessor(CustomLazyImport)
        text = "from math import sqrt"
        processed_text = processor._convert_from_str(text)
        assert processed_text == 'lazy_import(\'math\').sqrt', f"Expected 'lazy_import(\'math\').sqrt' but got {processed_text}"
    
    def test_malformed_input(self):
        """
        Test that an error is raised for malformed input.
        """
        processor = ImportProcessor()
        with pytest.raises(ValueError) as excinfo:
            processor._convert_from_str('invalid input')
        assert str(excinfo.value) == 'bad from/import \'invalid input\'', f"Expected error message to be 'bad from/import \'invalid input\'' but got {excinfo.value}"
    
    def test_process_text(self):
        """
        Test the process_text method with a simple import statement.
        """
        processor = ImportProcessor()
        text = "from math import sqrt"
        processed_text = processor.process_text(text)
        assert processed_text == 'lazy_import(\'math\').sqrt', f"Expected 'lazy_import(\'math\').sqrt' but got {processed_text}"
    
    def test_import_name_collision(self):
        """
        Test that an error is raised when there is a name collision.
        """
        processor = ImportProcessor()
        with pytest.raises(ImportNameCollision) as excinfo:
            processor._convert_from_str('from math import sqrt')
            processor._convert_from_str('from math import sqrt')
        assert str(excinfo.value) == 'Import name collision: sqrt', f"Expected error message to be 'Import name collision: sqrt' but got {excinfo.value}"

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
_ ERROR collecting test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0.py:3: in <module>
    from pytutils.lazy import ImportReplacer
E   ImportError: cannot import name 'ImportReplacer' from 'pytutils.lazy' (/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""