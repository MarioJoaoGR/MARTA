
import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer
from pytest import raises as pytest_raises  # Renamed for clarity and consistency with PEP8

# Test cases for _canonicalize_import_text method
def test_canonicalize_import_text():
    processor = ImportProcessor()
    
    # Test case 1: Simple imports
    text = '''
    from bzrlib import (
        foo,
        bar,
        baz,
    )
    import bzrlib.branch
    import bzrlib.transport
    '''
    expected_output = [
        'from bzrlib import foo',
        'from bzrlib import bar',
        'from bzrlib import baz',
        'import bzrlib.branch',
        'import bzrlib.transport'
    ]
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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0.py F [100%]

=================================== FAILURES ===================================
________________________ test_canonicalize_import_text _________________________

    def test_canonicalize_import_text():
        processor = ImportProcessor()
    
        # Test case 1: Simple imports
        text = '''
        from bzrlib import (
            foo,
            bar,
            baz,
        )
        import bzrlib.branch
        import bzrlib.transport
        '''
        expected_output = [
            'from bzrlib import foo',
            'from bzrlib import bar',
            'from bzrlib import baz',
            'import bzrlib.branch',
            'import bzrlib.transport'
        ]
>       assert processor._canonicalize_import_text(text) == expected_output, f"Expected {expected_output}, but got {processor._canonicalize_import_text(text)}"
E       AssertionError: Expected ['from bzrlib import foo', 'from bzrlib import bar', 'from bzrlib import baz', 'import bzrlib.branch', 'import bzrlib.transport'], but got ['from bzrlib import  foo, bar, baz, ', 'import bzrlib.branch', 'import bzrlib.transport']
E       assert ['from bzrlib...ib.transport'] == ['from bzrlib...ib.transport']
E         
E         At index 0 diff: 'from bzrlib import  foo, bar, baz, ' != 'from bzrlib import foo'
E         Right contains 2 more items, first extra item: 'import bzrlib.branch'
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0.py::test_canonicalize_import_text
============================== 1 failed in 0.05s ===============================
"""