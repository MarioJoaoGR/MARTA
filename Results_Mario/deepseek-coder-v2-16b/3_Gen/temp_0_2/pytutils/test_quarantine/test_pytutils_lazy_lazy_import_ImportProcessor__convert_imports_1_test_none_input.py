
import pytest
from pytutils.lazy import lazy_import

@pytest.fixture
def processor():
    return lazy_import.ImportProcessor()

def test_none_input(processor):
    scope = {}
    processor._convert_imports(scope)
    assert len(processor.imports) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

processor = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7fc090e37430>

    def test_none_input(processor):
        scope = {}
>       processor._convert_imports(scope)

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_1_test_none_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7fc090e37430>
scope = {}

    def _convert_imports(self, scope):
        # Now convert the map into a set of imports
>       for name, info in self.imports.iteritems():
E       AttributeError: 'dict' object has no attribute 'iteritems'

pytutils/pytutils/lazy/lazy_import.py:322: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_1_test_none_input.py::test_none_input
============================== 1 failed in 0.09s ===============================
"""