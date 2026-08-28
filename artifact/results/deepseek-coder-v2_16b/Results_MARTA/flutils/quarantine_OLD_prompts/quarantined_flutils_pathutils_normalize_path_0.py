
import os
from pathlib import Path
from flutils.pathutils import normalize_path
import pytest
from unittest.mock import patch


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_case_posix _____________________________

    def test_valid_case_posix():
        with patch('os.getcwd', return_value='/current/working/dir'):
            normalized_path = normalize_path('~/tmp/foo/../bar')
>           assert str(normalized_path) == '/home/test_user/tmp/bar'
E           AssertionError: assert '/home/joaovitorino/tmp/bar' == '/home/test_user/tmp/bar'
E             
E             - /home/test_user/tmp/bar
E             + /home/joaovitorino/tmp/bar

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_0.py:11: AssertionError
___________________________ test_valid_case_windows ____________________________

    def test_valid_case_windows():
        with patch('os.getcwd', return_value='/current/working/dir'):
            normalized_path = normalize_path('C:/Users/username/Documents/foo/../bar')
>           assert str(normalized_path) == 'C:/Users/username/Documents/bar'
E           AssertionError: assert '/current/wor...Documents/bar' == 'C:/Users/use...Documents/bar'
E             
E             - C:/Users/username/Documents/bar
E             + /current/working/dir/C:/Users/username/Documents/bar

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_0.py::test_valid_case_posix
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_0.py::test_valid_case_windows
============================== 2 failed in 0.05s ===============================
"""