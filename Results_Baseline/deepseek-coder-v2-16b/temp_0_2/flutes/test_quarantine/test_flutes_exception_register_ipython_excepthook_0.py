
import pytest
from flutes.exception import register_ipython_excepthook
import sys
from IPython.core import ultratb
from bdb import BdbQuit

# Test default usage without capturing KeyboardInterrupt
def test_register_ipython_excepthook_default():
    register_ipython_excepthook(capture_keyboard_interrupt=False)
    # Simulate an exception to trigger the excepthook
    try:
        raise Exception("Test exception")
    except Exception as e:
        pass  # The excepthook will handle this, but not KeyboardInterrupt

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
___________________ test_register_ipython_excepthook_default ___________________

    def test_register_ipython_excepthook_default():
        register_ipython_excepthook(capture_keyboard_interrupt=False)
        # Simulate an exception to trigger the excepthook
        try:
            raise Exception("Test exception")
        except Exception as e:
            pass  # The excepthook will handle this, but not KeyboardInterrupt
    
>       assert sys.excepthook == ultratb.FormattedTB(mode='Context', color_scheme='Linux', call_pdb=1)
E       AssertionError: assert <function register_ipython_excepthook.<locals>.excepthook at 0x7f0d2ecb0040> == <IPython.core.ultratb.FormattedTB object at 0x7f0d2ec132d0>
E        +  where <function register_ipython_excepthook.<locals>.excepthook at 0x7f0d2ecb0040> = sys.excepthook
E        +  and   <IPython.core.ultratb.FormattedTB object at 0x7f0d2ec132d0> = <class 'IPython.core.ultratb.FormattedTB'>(mode='Context', color_scheme='Linux', call_pdb=1)
E        +    where <class 'IPython.core.ultratb.FormattedTB'> = ultratb.FormattedTB

flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0.py::test_register_ipython_excepthook_default
========================= 1 failed, 1 passed in 0.42s ==========================
"""