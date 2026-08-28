
import pytest
from flutes.iterator import split_by




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_separator ___________________________

    def test_valid_case_separator():
        result = list(split_by(" Split by: ", empty_segments=True, separator='.'))
        expected = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
>       assert result == expected
E       AssertionError: assert [[' ', 'S', '...i', 't', ...]] == [[], ['S', 'p...'y', ':'], []]
E         
E         At index 0 diff: [' ', 'S', 'p', 'l', 'i', 't', ' ', 'b', 'y', ':', ' '] != []
E         Right contains 3 more items, first extra item: ['S', 'p', 'l', 'i', 't']
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py:8: AssertionError
__________________________ test_valid_case_criterion ___________________________

    def test_valid_case_criterion():
        result = list(split_by(" Split by: ", empty_segments=True, criterion=lambda x: x == '.'))
        expected = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
>       assert result == expected
E       AssertionError: assert [[' ', 'S', '...i', 't', ...]] == [[], ['S', 'p...'y', ':'], []]
E         
E         At index 0 diff: [' ', 'S', 'p', 'l', 'i', 't', ' ', 'b', 'y', ':', ' '] != []
E         Right contains 3 more items, first extra item: ['S', 'p', 'l', 'i', 't']
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py:13: AssertionError
_____________________________ test_empty_segments ______________________________

    def test_empty_segments():
        result = list(split_by(" Split by: ", empty_segments=True, separator='.'))
        expected = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
>       assert result == expected
E       AssertionError: assert [[' ', 'S', '...i', 't', ...]] == [[], ['S', 'p...'y', ':'], []]
E         
E         At index 0 diff: [' ', 'S', 'p', 'l', 'i', 't', ' ', 'b', 'y', ':', ' '] != []
E         Right contains 3 more items, first extra item: ['S', 'p', 'l', 'i', 't']
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py:18: AssertionError
____________________________ test_no_empty_segments ____________________________

    def test_no_empty_segments():
        result = list(split_by(" Split by: ", empty_segments=False, separator='.'))
        expected = [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]
>       assert result == expected
E       AssertionError: assert [[' ', 'S', '...i', 't', ...]] == [['S', 'p', '...b', 'y', ':']]
E         
E         At index 0 diff: [' ', 'S', 'p', 'l', 'i', 't', ' ', 'b', 'y', ':', ' '] != ['S', 'p', 'l', 'i', 't']
E         Right contains one more item: ['b', 'y', ':']
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py::test_valid_case_separator
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py::test_valid_case_criterion
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py::test_empty_segments
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_1.py::test_no_empty_segments
============================== 4 failed in 0.08s ===============================
"""