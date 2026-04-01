
import pytest
from pymonet.semigroups import Last, Semigroup

def test_invalid_inputs():
    with pytest.raises(TypeError):
        l1 = Last(5)  # Create a Last instance with an initial value of 5
        try:
            l1.concat('not a Semigroup')  # Attempt to concat with invalid input
        except AttributeError as e:
            assert str(e) == "AttributeError: 'str' object has no attribute 'value'"

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            l1 = Last(5)  # Create a Last instance with an initial value of 5
            try:
>               l1.concat('not a Semigroup')  # Attempt to concat with invalid input

pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_2_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.semigroups.Last object at 0x7f937b634310>
semigroup = 'not a Semigroup'

    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Last[B]
        :returns: new Last with last value
        :rtype: Last[A]
        """
>       return Last(semigroup.value)
E       AttributeError: 'str' object has no attribute 'value'

pyMonet/pymonet/semigroups.py:117: AttributeError

During handling of the above exception, another exception occurred:

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            l1 = Last(5)  # Create a Last instance with an initial value of 5
            try:
                l1.concat('not a Semigroup')  # Attempt to concat with invalid input
            except AttributeError as e:
>               assert str(e) == "AttributeError: 'str' object has no attribute 'value'"
E               assert "'str' object...ibute 'value'" == "AttributeErr...ibute 'value'"
E                 
E                 - AttributeError: 'str' object has no attribute 'value'
E                 ? ----------------
E                 + 'str' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_2_test_invalid_inputs.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""