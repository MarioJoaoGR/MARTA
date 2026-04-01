
from pymonet.validation import Validation

def test_edge_case_none():
    val = Validation(None, ['Initial error'])
    
    def add_one(x):
        if x is not None:
            return Validation(x + 1, [])
        else:
            return Validation(None, ["Value must be positive"])
    
    result = val.bind(add_one)
    
    assert result.value is None
    assert result.errors == ['Initial error', 'Value must be positive']

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_bind_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        val = Validation(None, ['Initial error'])
    
        def add_one(x):
            if x is not None:
                return Validation(x + 1, [])
            else:
                return Validation(None, ["Value must be positive"])
    
        result = val.bind(add_one)
    
        assert result.value is None
>       assert result.errors == ['Initial error', 'Value must be positive']
E       AssertionError: assert ['Value must be positive'] == ['Initial err... be positive']
E         
E         At index 0 diff: 'Value must be positive' != 'Initial error'
E         Right contains one more item: 'Value must be positive'
E         Use -v to get more diff

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_bind_1_test_edge_case_none.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_bind_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.08s ===============================
"""