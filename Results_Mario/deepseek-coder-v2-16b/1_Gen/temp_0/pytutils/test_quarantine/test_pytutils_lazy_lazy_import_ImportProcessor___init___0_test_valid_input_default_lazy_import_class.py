
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_valid_input_default_lazy_import_class():
    # Test initialization with default lazy import class
    processor = ImportProcessor()
    
    assert isinstance(processor._lazy_import_class, ImportReplacer)

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor___init___0_test_valid_input_default_lazy_import_class.py F [100%]

=================================== FAILURES ===================================
__________________ test_valid_input_default_lazy_import_class __________________

    def test_valid_input_default_lazy_import_class():
        # Test initialization with default lazy import class
        processor = ImportProcessor()
    
>       assert isinstance(processor._lazy_import_class, ImportReplacer)
E       AssertionError: assert False
E        +  where False = isinstance(<class 'pytutils.lazy.lazy_import.ImportReplacer'>, ImportReplacer)
E        +    where <class 'pytutils.lazy.lazy_import.ImportReplacer'> = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7f5458ec5c00>._lazy_import_class

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor___init___0_test_valid_input_default_lazy_import_class.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor___init___0_test_valid_input_default_lazy_import_class.py::test_valid_input_default_lazy_import_class
============================== 1 failed in 0.05s ===============================
"""