
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
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py F [100%]

=================================== FAILURES ===================================
________________________ test_edge_case_empty_segments _________________________

    def test_edge_case_empty_segments():
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

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_split_by_0.py::test_edge_case_empty_segments
============================== 1 failed in 0.07s ===============================
"""