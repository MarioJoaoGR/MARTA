
from httpie.utils import split_iterable
from unittest.mock import patch
import pytest

def test_edge_case():
    with patch('httpie.utils.split_iterable', autospec=True) as mock_split:
        # Test None input
        mock_split.return_value = ([], [])
        assert split_iterable(None, lambda x: True) == ([], [])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_iterable_5_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with patch('httpie.utils.split_iterable', autospec=True) as mock_split:
            # Test None input
            mock_split.return_value = ([], [])
>           assert split_iterable(None, lambda x: True) == ([], [])

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_iterable_5_test_edge_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iterable = None
key = <function test_edge_case.<locals>.<lambda> at 0x7fa426522700>

    def split_iterable(iterable: Iterable[T], key: Callable[[T], bool]) -> Tuple[List[T], List[T]]:
        left, right = [], []
>       for item in iterable:
E       TypeError: 'NoneType' object is not iterable

httpie/httpie/utils.py:250: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_iterable_5_test_edge_case.py::test_edge_case
============================== 1 failed in 0.17s ===============================
"""