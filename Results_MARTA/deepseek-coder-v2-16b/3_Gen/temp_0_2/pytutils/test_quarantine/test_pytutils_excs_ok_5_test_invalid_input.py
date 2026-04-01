
import pytest
from pytutils.excs import ok

def test_ok():
    with pytest.raises(ValueError):
        with ok('NotAValidException'):
            int('abc')

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

pytutils/Test4DT_tests/test_pytutils_excs_ok_5_test_invalid_input.py F   [100%]

=================================== FAILURES ===================================
___________________________________ test_ok ____________________________________

    def test_ok():
        with pytest.raises(ValueError):
            with ok('NotAValidException'):
>               int('abc')
E               ValueError: invalid literal for int() with base 10: 'abc'

pytutils/Test4DT_tests/test_pytutils_excs_ok_5_test_invalid_input.py:8: ValueError

During handling of the above exception, another exception occurred:

    def test_ok():
        with pytest.raises(ValueError):
>           with ok('NotAValidException'):

pytutils/Test4DT_tests/test_pytutils_excs_ok_5_test_invalid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/contextlib.py:158: in __exit__
    self.gen.throw(typ, value, traceback)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

exceptions = ('NotAValidException',)

    @contextmanager
    def ok(*exceptions):
        """Context manager to pass exceptions.
        :param exceptions: Exceptions to pass
        """
        try:
            yield
        except Exception as e:
>           if isinstance(e, exceptions):
E           TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

pytutils/pytutils/excs.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_excs_ok_5_test_invalid_input.py::test_ok
============================== 1 failed in 0.07s ===============================
"""