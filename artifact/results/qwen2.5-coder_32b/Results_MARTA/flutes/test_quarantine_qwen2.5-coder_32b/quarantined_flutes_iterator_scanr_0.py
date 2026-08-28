
import pytest
from flutes.iterator import scanr






"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 6 items

../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        result = scanr(lambda acc, x: acc + [x], [1, 2, 3], [])
>       assert result == [[], [3], [3, 2], [3, 2, 1]]
E       assert [[3, 2, 1], [3, 2], [3], []] == [[], [3], [3, 2], [3, 2, 1]]
E         
E         At index 0 diff: [3, 2, 1] != []
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py:7: AssertionError
__________________ test_invalid_iterable_non_iterable_string ___________________

    def test_invalid_iterable_non_iterable_string():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py:10: Failed
_________________________ test_single_element_iterable _________________________

    def test_single_element_iterable():
        result = scanr(lambda acc, x: acc + [x], [1], [])
>       assert result == [[], [1]]
E       assert [[1], []] == [[], [1]]
E         
E         At index 0 diff: [1] != []
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py:15: AssertionError
____________________ test_multiplication_with_initial_value ____________________

    def test_multiplication_with_initial_value():
        result = scanr(lambda acc, x: acc * x, [1, 2, 3, 4], 1)
>       assert result == [1, 4, 12, 24, 96]
E       assert [24, 24, 12, 4, 1] == [1, 4, 12, 24, 96]
E         
E         At index 0 diff: 24 != 1
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py:19: AssertionError
________________________ test_concatenation_of_strings _________________________

    def test_concatenation_of_strings():
        result = scanr(lambda acc, x: acc + x, ["a", "b", "c"], "")
>       assert result == ['', 'c', 'cb', 'cba']
E       AssertionError: assert ['cba', 'cb', 'c', ''] == ['', 'c', 'cb', 'cba']
E         
E         At index 0 diff: 'cba' != ''
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py:23: AssertionError
_____________________ test_subtraction_with_initial_value ______________________

    def test_subtraction_with_initial_value():
        result = scanr(lambda acc, x: acc - x, [1, 2, 3], 10)
>       assert result == [10, 9, 7, 4]
E       assert [4, 5, 7, 10] == [10, 9, 7, 4]
E         
E         At index 0 diff: 4 != 10
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py::test_invalid_iterable_non_iterable_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py::test_single_element_iterable
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py::test_multiplication_with_initial_value
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py::test_concatenation_of_strings
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_qwen2.5-coder_32b/test_flutes_iterator_scanr_0.py::test_subtraction_with_initial_value
============================== 6 failed in 0.08s ===============================
"""