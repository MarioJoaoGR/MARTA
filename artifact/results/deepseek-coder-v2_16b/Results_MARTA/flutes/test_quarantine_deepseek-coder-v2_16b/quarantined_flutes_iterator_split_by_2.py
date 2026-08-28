
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

../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_separator ___________________________

    def test_valid_case_separator():
        iterable = " Split by: "
        empty_segments = True
        separator = '.'
        result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
>       assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
E       AssertionError: assert [[' ', 'S', '...i', 't', ...]] == [[], ['S', 'p...'y', ':'], []]
E         
E         At index 0 diff: [' ', 'S', 'p', 'l', 'i', 't', ' ', 'b', 'y', ':', ' '] != []
E         Right contains 3 more items, first extra item: ['S', 'p', 'l', 'i', 't']
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_2.py:10: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        iterable = " Split by: "
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_2.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_2.py::test_valid_case_separator
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_2.py::test_error_case
============================== 2 failed in 0.07s ===============================
"""