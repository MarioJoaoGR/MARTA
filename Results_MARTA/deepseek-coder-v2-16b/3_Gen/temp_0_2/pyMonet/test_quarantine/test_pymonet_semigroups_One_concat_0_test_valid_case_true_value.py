
import pytest
from pymonet.semigroups import One

def test_valid_case_true_value():
    # Test with True value
    one1 = One(False)  # Instantiating with False
    one2 = One(True)   # Instantiating with True
    combined_one = one1.concat(one2)  # Combining the two Monoids
    assert combined_one.value is True, "Expected value to be True"
    
    # Test with a falsy value and False
    another_one = One(0)               # Instantiating with a falsy value (integer 0)
    combined_with_zero = another_one.concat(One(False))  # Combining with False
    assert combined_with_zero.value is True, "Expected value to be True"

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_0_test_valid_case_true_value.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_true_value __________________________

    def test_valid_case_true_value():
        # Test with True value
        one1 = One(False)  # Instantiating with False
        one2 = One(True)   # Instantiating with True
        combined_one = one1.concat(one2)  # Combining the two Monoids
        assert combined_one.value is True, "Expected value to be True"
    
        # Test with a falsy value and False
        another_one = One(0)               # Instantiating with a falsy value (integer 0)
        combined_with_zero = another_one.concat(One(False))  # Combining with False
>       assert combined_with_zero.value is True, "Expected value to be True"
E       AssertionError: Expected value to be True
E       assert False is True
E        +  where False = <pymonet.semigroups.One object at 0x7fa173ae3290>.value

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_0_test_valid_case_true_value.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_0_test_valid_case_true_value.py::test_valid_case_true_value
============================== 1 failed in 0.08s ===============================
"""