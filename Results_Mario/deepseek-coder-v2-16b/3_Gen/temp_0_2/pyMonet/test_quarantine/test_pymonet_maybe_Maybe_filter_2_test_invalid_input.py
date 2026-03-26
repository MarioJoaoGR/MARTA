
from pymonet.maybe import Maybe

def test_invalid_input():
    # Test with None value and a filterer function that should return False
    maybe_none = Maybe(value=None, is_nothing=False)
    filtered_maybe = maybe_none.filter(lambda x: x > 10)
    
    assert maybe_none.is_nothing == True
    assert filtered_maybe.is_nothing == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_filter_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with None value and a filterer function that should return False
        maybe_none = Maybe(value=None, is_nothing=False)
>       filtered_maybe = maybe_none.filter(lambda x: x > 10)

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_filter_2_test_invalid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/maybe.py:97: in filter
    if self.is_nothing or not filterer(self.value):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None

>   filtered_maybe = maybe_none.filter(lambda x: x > 10)
E   TypeError: '>' not supported between instances of 'NoneType' and 'int'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_filter_2_test_invalid_input.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_filter_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""