
import pytest
from unittest.mock import patch
import os
import collections
import typing
from pytutils.env import load_env_file


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
        with patch('os.environ', {'HOME': '/home/user'}):
            result = load_env_file(lines)
>           assert result == collections.OrderedDict([('TEST', '/home/user/yeee-:$PATH'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
E           AssertionError: assert OrderedDict([..._NOT_EXIST')]) == OrderedDict([..._NOT_EXIST')])
E             
E             Differing items:
E             {'YOLO': '/home/user/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'} != {'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}
E             {'THISIS': '/home/user/a/test'} != {'THISIS': '~/a/test'}
E             {'TEST': '/home/user/yeee-$PATH'} != {'TEST': '/home/user/yeee-:$PATH'}
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_1.py:13: AssertionError
__________________________ test_invalid_format_input ___________________________

    def test_invalid_format_input():
        lines = ['INVALIDFORMAT', 'THISIS=~/a/test']
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_1.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_1.py::test_invalid_format_input
============================== 2 failed in 0.05s ===============================
"""