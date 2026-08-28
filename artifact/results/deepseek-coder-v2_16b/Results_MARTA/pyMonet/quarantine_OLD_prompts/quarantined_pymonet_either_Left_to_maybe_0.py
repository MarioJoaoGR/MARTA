
import pytest
from pymonet.either import Left, Right
from pymonet.maybe import Maybe


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_either_Left_to_maybe_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_left_to_maybe ______________________________

    def test_left_to_maybe():
        left_instance = Left("error message")
        maybe_result = left_instance.to_maybe()
        assert isinstance(maybe_result, Maybe)
>       assert maybe_result.is_nothing()
E       TypeError: 'bool' object is not callable

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_either_Left_to_maybe_0.py:10: TypeError
____________________________ test_right_no_to_maybe ____________________________

    def test_right_no_to_maybe():
        right_instance = Right("valid value")
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_either_Left_to_maybe_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_either_Left_to_maybe_0.py::test_left_to_maybe
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_either_Left_to_maybe_0.py::test_right_no_to_maybe
============================== 2 failed in 0.07s ===============================
"""