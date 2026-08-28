
import pytest
from pathlib import Path
import os
from flutils.pathutils import normalize_path







"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 7 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py F [ 14%]
FFFFFF                                                                   [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        raw_path = '~/tmp/foo/../bar'
        normalized_path = normalize_path(raw_path)
>       assert str(normalized_path) == (Path.home() / 'tmp' / 'bar')
E       AssertionError: assert '/home/joaovitorino/tmp/bar' == ((PosixPath('/home/joaovitorino') / 'tmp') / 'bar')
E        +  where '/home/joaovitorino/tmp/bar' = str(PosixPath('/home/joaovitorino/tmp/bar'))
E        +  and   PosixPath('/home/joaovitorino') = home()
E        +    where home = Path.home

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py:10: AssertionError
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        raw_path = 'C:/Users/username/Documents/foo/../bar'
        normalized_path = normalize_path(raw_path)
>       assert str(normalized_path) == Path('C:/Users/username/Documents/bar')
E       AssertionError: assert '/data/results/harness/sandbox/marta/C:/Users/username/Documents/bar' == PosixPath('C:/Users/username/Documents/bar')
E        +  where '/data/results/harness/sandbox/marta/C:/Users/username/Documents/bar' = str(PosixPath('/data/results/harness/sandbox/marta/C:/Users/username/Documents/bar'))
E        +  and   PosixPath('C:/Users/username/Documents/bar') = Path('C:/Users/username/Documents/bar')

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py:15: AssertionError
______________________________ test_valid_case_3 _______________________________

    def test_valid_case_3():
        raw_path = '~/tmp/foo/../bar'.encode('utf-8')
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py:19: Failed
______________________________ test_valid_case_4 _______________________________

    def test_valid_case_4():
>       raw_path = b'C:/Users/username/Documents/foo/../bar'.encode('utf-8')
E       AttributeError: 'bytes' object has no attribute 'encode'. Did you mean: 'decode'?

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py:23: AttributeError
______________________________ test_valid_case_5 _______________________________

    def test_valid_case_5():
        raw_path = Path('~/tmp/foo/../bar')
        normalized_path = normalize_path(raw_path)
>       assert str(normalized_path) == (Path.home() / 'tmp' / 'bar')
E       AssertionError: assert '/home/joaovitorino/tmp/bar' == ((PosixPath('/home/joaovitorino') / 'tmp') / 'bar')
E        +  where '/home/joaovitorino/tmp/bar' = str(PosixPath('/home/joaovitorino/tmp/bar'))
E        +  and   PosixPath('/home/joaovitorino') = home()
E        +    where home = Path.home

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py:30: AssertionError
______________________________ test_valid_case_6 _______________________________

    def test_valid_case_6():
        raw_path = Path('C:/Users/username/Documents/foo/../bar')
        normalized_path = normalize_path(raw_path)
>       assert str(normalized_path) == Path('C:/Users/username/Documents/bar')
E       AssertionError: assert '/data/results/harness/sandbox/marta/C:/Users/username/Documents/bar' == PosixPath('C:/Users/username/Documents/bar')
E        +  where '/data/results/harness/sandbox/marta/C:/Users/username/Documents/bar' = str(PosixPath('/data/results/harness/sandbox/marta/C:/Users/username/Documents/bar'))
E        +  and   PosixPath('C:/Users/username/Documents/bar') = Path('C:/Users/username/Documents/bar')

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py:35: AssertionError
____________________________ test_error_handling_2 _____________________________

    def test_error_handling_2():
        raw_path = 'non/existent/path'
>       with pytest.raises(FileNotFoundError):
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py:39: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py::test_valid_case_2
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py::test_valid_case_3
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py::test_valid_case_4
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py::test_valid_case_5
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py::test_valid_case_6
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_normalize_path_1.py::test_error_handling_2
============================== 7 failed in 0.07s ===============================
"""