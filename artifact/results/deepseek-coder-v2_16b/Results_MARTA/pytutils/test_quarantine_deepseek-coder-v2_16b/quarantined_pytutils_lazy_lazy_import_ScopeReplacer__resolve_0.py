
import pytest
from pytutils.lazy.lazy_import import lazy_import


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_lazy_import_successful __________________________

    def test_lazy_import_successful():
        """Test that lazy_import can successfully import a module and function."""
>       pf = lazy_import('pygmentize', 'pygments.formatters.get_formatter_by_name')

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/lazy_import.py:475: in lazy_import
    return proc.lazy_import(scope, text)
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/lazy_import.py:317: in lazy_import
    self._build_map(text)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7f206c1b56f0>
text = 'pygments.formatters.get_formatter_by_name'

    def _build_map(self, text):
        """Take a string describing imports, and build up the internal map"""
        for line in self._canonicalize_import_text(text):
            if line.startswith('import '):
                self._convert_import_str(line)
            elif line.startswith('from '):
                self._convert_from_str(line)
            else:
>               raise errors.InvalidImportLine(line,
                    "doesn't start with 'import ' or 'from '")
E               NameError: name 'errors' is not defined

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/lazy_import.py:334: NameError
___________________________ test_lazy_import_failure ___________________________

    def test_lazy_import_failure():
        """Test that lazy_import raises an error when the module or function cannot be imported."""
        with pytest.raises(ImportError):
>           lazy_import('nonexistentmodule', 'nonexistentfunction')

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/lazy_import.py:475: in lazy_import
    return proc.lazy_import(scope, text)
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/lazy_import.py:317: in lazy_import
    self._build_map(text)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7f206c207850>
text = 'nonexistentfunction'

    def _build_map(self, text):
        """Take a string describing imports, and build up the internal map"""
        for line in self._canonicalize_import_text(text):
            if line.startswith('import '):
                self._convert_import_str(line)
            elif line.startswith('from '):
                self._convert_from_str(line)
            else:
>               raise errors.InvalidImportLine(line,
                    "doesn't start with 'import ' or 'from '")
E               NameError: name 'errors' is not defined

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/lazy/lazy_import.py:334: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0.py::test_lazy_import_successful
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0.py::test_lazy_import_failure
============================== 2 failed in 0.06s ===============================
"""