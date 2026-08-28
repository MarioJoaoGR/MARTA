
import pytest
from mimesis.random import Random



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_Random_custom_code_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_valid_input_default_parameters ______________________

    def test_valid_input_default_parameters():
        rand_gen = Random()
        code = rand_gen.custom_code()
        assert isinstance(code, str), "Expected a string"
>       assert len(code) == 3, f"Expected length of 3, got {len(code)}"
E       AssertionError: Expected length of 3, got 4
E       assert 4 == 3
E        +  where 4 = len('S023')

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_Random_custom_code_0.py:9: AssertionError
____________________ test_custom_mask_with_only_characters _____________________

    def test_custom_mask_with_only_characters():
        rand_gen = Random()
        code = rand_gen.custom_code('@##')
        assert isinstance(code, str), "Expected a string"
>       assert len(code) == 2, f"Expected length of 2, got {len(code)}"
E       AssertionError: Expected length of 2, got 3
E       assert 3 == 2
E        +  where 3 = len('E42')

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_Random_custom_code_0.py:15: AssertionError
____________________ test_invalid_placeholder_same_as_digit ____________________

    def test_invalid_placeholder_same_as_digit():
        rand_gen = Random()
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_Random_custom_code_0.py:19: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_Random_custom_code_0.py::test_valid_input_default_parameters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_Random_custom_code_0.py::test_custom_mask_with_only_characters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_Random_custom_code_0.py::test_invalid_placeholder_same_as_digit
============================== 3 failed in 0.15s ===============================
"""