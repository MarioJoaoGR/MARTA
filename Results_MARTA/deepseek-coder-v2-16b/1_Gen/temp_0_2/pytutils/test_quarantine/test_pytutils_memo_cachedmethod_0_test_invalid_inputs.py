
import pytest
from pytutils.memo import cachedmethod

def test_invalid_inputs():
    @cachedmethod(lambda inst: {}, key=lambda inst, *args: args[0])
    def method(self, arg1):
        if isinstance(arg1, bool) or arg1 == 0 or not arg1:
            raise TypeError("Expected a non-boolean, non-zero value")
        return arg1 * 2

    with pytest.raises(TypeError):
        method(None, True)
    with pytest.raises(TypeError):
        method(None, False)
    with pytest.raises(TypeError):
        method(None, 0)
    with pytest.raises(TypeError):
        method(None, "")

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

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       @cachedmethod(lambda inst: {}, key=lambda inst, *args: args[0])

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_invalid_inputs.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

method = <function test_invalid_inputs.<locals>.method at 0x7f876d0e76a0>

    def decorator(method):
        # pass method to default key function for backwards compatibilty
        if key is _default:
            makekey = functools.partial(cachetools.typedkey if typed else cachetools.hashkey, method)
        else:
            makekey = key  # custom key function always receive method args
    
>       @six.wraps(method)
E       NameError: name 'six' is not defined

pytutils/pytutils/memo.py:43: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.06s ===============================
"""