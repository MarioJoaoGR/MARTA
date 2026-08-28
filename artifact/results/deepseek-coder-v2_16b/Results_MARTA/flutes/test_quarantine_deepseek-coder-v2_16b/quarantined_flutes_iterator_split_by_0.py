
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_split_by_with_separator _________________________

    def test_split_by_with_separator():
        iterable = " Split by: "
        result = list(split_by(iterable, separator='.'))
        expected = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
>       assert result == expected
E       AssertionError: assert [[' ', 'S', '...i', 't', ...]] == [[], ['S', 'p...'y', ':'], []]
E         
E         At index 0 diff: [' ', 'S', 'p', 'l', 'i', 't', ' ', 'b', 'y', ':', ' '] != []
E         Right contains 3 more items, first extra item: ['S', 'p', 'l', 'i', 't']
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py:9: AssertionError
_________________________ test_split_by_empty_segments _________________________

    def test_split_by_empty_segments():
        iterable = [1, 2, 3, 6]
        result = list(split_by(iterable, separator='.'))
        expected = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
>       assert result == expected
E       AssertionError: assert [[1, 2, 3, 6]] == [[], ['S', 'p...'y', ':'], []]
E         
E         At index 0 diff: [1, 2, 3, 6] != []
E         Right contains 3 more items, first extra item: ['S', 'p', 'l', 'i', 't']
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py::test_split_by_with_separator
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py::test_split_by_empty_segments
============================== 2 failed in 0.07s ===============================
"""