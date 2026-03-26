
# Module: pytutils.lazy.lazy_import
# test_lazy_import.py
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer
try:
    from bzrlib import lazy_import
except ImportError:
    pass  # This will be handled in the tests themselves

def test_default_init():
    processor = ImportProcessor()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor___init___0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_default_init _______________________________

    def test_default_init():
        processor = ImportProcessor()
>       assert isinstance(processor._lazy_import_class, ImportReplacer)
E       AssertionError: assert False
E        +  where False = isinstance(<class 'pytutils.lazy.lazy_import.ImportReplacer'>, ImportReplacer)
E        +    where <class 'pytutils.lazy.lazy_import.ImportReplacer'> = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7f531e28ded0>._lazy_import_class

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor___init___0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor___init___0.py::test_default_init
========================= 1 failed, 1 passed in 0.06s ==========================
"""