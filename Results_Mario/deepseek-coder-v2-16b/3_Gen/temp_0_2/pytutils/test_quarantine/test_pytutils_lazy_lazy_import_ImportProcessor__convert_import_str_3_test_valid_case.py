
from pytutils.lazy.lazy_import import ImportProcessor

def test_valid_case():
    processor = ImportProcessor()
    
    # Test a simple import string
    processor._convert_import_str('import math')
    assert 'math' in processor.imports
    assert processor.imports['math'] == ([], None, {})

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_3_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        processor = ImportProcessor()
    
        # Test a simple import string
        processor._convert_import_str('import math')
        assert 'math' in processor.imports
>       assert processor.imports['math'] == ([], None, {})
E       AssertionError: assert (['math'], None, {}) == ([], None, {})
E         
E         At index 0 diff: ['math'] != []
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_3_test_valid_case.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_3_test_valid_case.py::test_valid_case
============================== 1 failed in 0.07s ===============================
"""