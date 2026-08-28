
import pytest
from pymonet.validation import Validation



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_validation_Validation_to_either_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_apply_function ______________________________

    def test_apply_function():
        def add_two(val):
            return val + 2
    
        val = Validation(value=5, errors=[])
>       applied_validation = val.ap(add_two)

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_validation_Validation_to_either_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.validation.Validation object at 0x7f19c8206c50>
fn = <function test_apply_function.<locals>.add_two at 0x7f19c8192170>

    def ap(self, fn):
        """
        It takes as a parameter function returning another Validation.
        Function is called with Validation value and returns new Validation with previous value
        and concated new and old errors.
    
        :param monad: monad contains function
        :type monad: Function(A) -> Validation[Any, List[E]]
        :returns: new validation with stored errors
        :rtype: Validation[A, List[E]]
        """
>       return Validation(self.value, self.errors + fn(self.value).errors)
E       AttributeError: 'int' object has no attribute 'errors'

/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/validation.py:96: AttributeError
________________________ test_apply_function_with_error ________________________

    def test_apply_function_with_error():
        def add_two(val):
            return Validation(value=val + 2, errors=[])
    
        val = Validation(value=5, errors=['Initial error'])
        applied_validation = val.ap(add_two)
    
>       assert applied_validation.value == 7
E       assert 5 == 7
E        +  where 5 = <pymonet.validation.Validation object at 0x7f19c8207ac0>.value

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_validation_Validation_to_either_0.py:22: AssertionError
___________________ test_apply_function_with_multiple_errors ___________________

    def test_apply_function_with_multiple_errors():
        def add_two(val):
            return Validation(value=val + 2, errors=['Additional error'])
    
        val = Validation(value=5, errors=['Initial error 1', 'Initial error 2'])
        applied_validation = val.ap(add_two)
    
>       assert applied_validation.value == 7
E       assert 5 == 7
E        +  where 5 = <pymonet.validation.Validation object at 0x7f19c8205060>.value

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_validation_Validation_to_either_0.py:33: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_validation_Validation_to_either_0.py::test_apply_function
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_validation_Validation_to_either_0.py::test_apply_function_with_error
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_validation_Validation_to_either_0.py::test_apply_function_with_multiple_errors
============================== 3 failed in 0.10s ===============================
"""