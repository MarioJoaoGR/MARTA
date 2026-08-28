
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, CustomLazyImport

class TestImportProcessor:
    """
    This class contains unit tests for the `ImportProcessor` class.
    """
    
    def test_default_lazy_import_class(self):
        """
        Test that the default lazy import class is ImportReplacer when no custom class is provided.
        """
        processor = ImportProcessor()
        assert isinstance(processor._lazy_import_class, ImportReplacer)
    
    def test_custom_lazy_import_class(self):
        """
        Test that the specified custom lazy import class is used when provided.
        """
        class CustomLazyImport(ImportReplacer):
            def replace_import(self, module_name):
                return f"lazy_import('{module_name}')"
        
        processor = ImportProcessor(CustomLazyImport)
        assert isinstance(processor._lazy_import_class, CustomLazyImport)
    
    def test_process_text(self):
        """
        Test that the `process_text` method replaces direct imports with lazy import statements.
        """
        processor = ImportProcessor()
        text = "from math import sqrt"
        processed_text = processor.process_text(text)
        assert processed_text == "lazy_import('math').sqrt"
    
    def test_build_map(self):
        """
        Test that the `_build_map` method correctly builds a map of imports from text.
        """
        processor = ImportProcessor()
        text = """
        from math import sqrt
        from os import path as op
        import sys
        """
        processor._build_map(text)
        assert 'math' in processor.imports and 'os' in processor.imports and 'sys' in processor.imports
        assert processor.imports['math'] == (['math'], None, {})
        assert processor.imports['os'] == (['os'], None, {'path': (['os', 'path'], 'op', {})})
        assert processor.imports['sys'] == (['sys'], None, {})
    
    def test_convert_imports(self):
        """
        Test that the `_convert_imports` method converts imports into lazy import requests in the given scope.
        """
        processor = ImportProcessor()
        processor.imports = {
            'foo': (['bzrlib', 'foo'], None, {'bar':(['bzrlib', 'foo', 'bar'], None, {})})
        }
        scope = {}
        processor._convert_imports(scope)
        assert 'lazy_import' in scope and 'baz' not in scope
        assert scope['lazy_import']('bzrlib.foo') == ImportReplacer
        assert scope['lazy_import']('bzrlib.foo.bar') == ImportReplacer

if __name__ == "__main__":
    pytest.main()

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
/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0.py:3: in <module>
    from pytutils.lazy.lazy_import import ImportReplacer, CustomLazyImport
E   ImportError: cannot import name 'CustomLazyImport' from 'pytutils.lazy.lazy_import' (/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/lazy_import.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""