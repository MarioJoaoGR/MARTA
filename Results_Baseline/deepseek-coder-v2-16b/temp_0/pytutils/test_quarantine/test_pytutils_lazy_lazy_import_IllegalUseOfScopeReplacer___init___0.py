
import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

# Test Case 1: Basic Usage of the Exception
def test_basic_usage():
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        raise IllegalUseOfScopeReplacer('my_function', 'Argument is not valid')
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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___init___0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
            raise IllegalUseOfScopeReplacer('my_function', 'Argument is not valid')
>       assert str(exc_info.value) == "ScopeReplacer object 'my_function' was used incorrectly: Argument is not valid"

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___init___0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_import.py:97: in __str__
    s = self._format()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[UnboundLocalError("cannot access local variable 'e' where it is not associated with a value") raised in repr()] IllegalUseOfScopeReplacer object at 0x7f470428ca60>

    def _format(self):
        s = getattr(self, '_preformatted_string', None)
        if s is not None:
            # contains a preformatted message
            return s
        try:
            fmt = self._get_format_string()
            if fmt:
                d = dict(self.__dict__)
                s = fmt % d
                # __str__() should always return a 'str' object
                # never a 'unicode' object.
                return s
        except Exception as e:
            pass # just bind to 'e' for formatting below
        else:
            e = None
        return 'Unprintable exception %s: dict=%r, fmt=%r, error=%r' \
            % (self.__class__.__name__,
               self.__dict__,
               getattr(self, '_fmt', None),
>              e)
E       UnboundLocalError: cannot access local variable 'e' where it is not associated with a value

pytutils/pytutils/lazy/lazy_import.py:83: UnboundLocalError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___init___0.py::test_basic_usage
========================= 1 failed, 1 passed in 0.06s ==========================
"""