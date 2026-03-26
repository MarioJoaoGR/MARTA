
import pytest
from pymonet.semigroups import Last

def test_invalid_input_error_handling():
    class OtherClass:
        pass
    
    other_instance = OtherClass()
    last_other = Last(other_instance)
    
    with pytest.raises(TypeError):
        # Attempt to concatenate a Last instance with an instance of a different class
        combined_last = last_other.concat(OtherClass())

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_2_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        class OtherClass:
            pass
    
        other_instance = OtherClass()
        last_other = Last(other_instance)
    
        with pytest.raises(TypeError):
            # Attempt to concatenate a Last instance with an instance of a different class
>           combined_last = last_other.concat(OtherClass())

pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_2_test_invalid_input_error_handling.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.semigroups.Last object at 0x7fcc995b9150>
semigroup = <Test4DT_tests.test_pymonet_semigroups_Last_concat_2_test_invalid_input_error_handling.test_invalid_input_error_handling.<locals>.OtherClass object at 0x7fcc995b91d0>

    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Last[B]
        :returns: new Last with last value
        :rtype: Last[A]
        """
>       return Last(semigroup.value)
E       AttributeError: 'OtherClass' object has no attribute 'value'

pyMonet/pymonet/semigroups.py:117: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.08s ===============================
"""