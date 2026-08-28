
import pytest
import itertools
import typing as T
from docstring_parser.numpydoc import _pairwise


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc__pairwise_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        iterable = [1, 2, 3, 4]
        result = list(_pairwise(iterable))
>       assert result == [(1, 2), (2, 3), (3, 4)]
E       assert [(1, 2), (2, ...4), (4, None)] == [(1, 2), (2, 3), (3, 4)]
E         
E         Left contains one more item: (4, None)
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc__pairwise_0.py:10: AssertionError
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        iterable = 'not iterable'
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc__pairwise_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc__pairwise_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc__pairwise_0.py::test_error_handling
============================== 2 failed in 0.05s ===============================
"""