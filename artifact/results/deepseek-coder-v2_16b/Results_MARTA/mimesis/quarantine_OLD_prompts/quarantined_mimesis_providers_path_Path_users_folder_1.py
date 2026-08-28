
import pytest
from unittest.mock import patch
from mimesis.providers.path import Path
from pathlib import PurePosixPath, PureWindowsPath
import sys

@pytest.fixture(params=['linux', 'darwin', 'win32', 'win64'])
def path_instance(request):
    with patch('sys.platform', request.param):
        yield Path(platform=request.param)

def test_path_instance_on_linux(path_instance):
    assert isinstance(path_instance._pathlib_home, PurePosixPath)

def test_path_instance_on_darwin(path_instance):
    assert isinstance(path_instance._pathlib_home, PurePosixPath)

def test_path_instance_on_windows32(path_instance):
    assert isinstance(path_instance._pathlib_home, PureWindowsPath)

def test_path_instance_on_windows64(path_instance):
    assert isinstance(path_instance._pathlib_home, PureWindowsPath)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 16 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py . [  6%]
FFF.FFFF...F...                                                          [100%]

=================================== FAILURES ===================================
_____________________ test_path_instance_on_linux[darwin] ______________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d141f1990>

    def test_path_instance_on_linux(path_instance):
>       assert isinstance(path_instance._pathlib_home, PurePosixPath)
E       AssertionError: assert False
E        +  where False = isinstance(PureWindowsPath('/home'), PurePosixPath)
E        +    where PureWindowsPath('/home') = <mimesis.providers.path.Path object at 0x7f7d141f1990>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:14: AssertionError
______________________ test_path_instance_on_linux[win32] ______________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d141f3880>

    def test_path_instance_on_linux(path_instance):
>       assert isinstance(path_instance._pathlib_home, PurePosixPath)
E       AssertionError: assert False
E        +  where False = isinstance(PureWindowsPath('C:/Users'), PurePosixPath)
E        +    where PureWindowsPath('C:/Users') = <mimesis.providers.path.Path object at 0x7f7d141f3880>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:14: AssertionError
______________________ test_path_instance_on_linux[win64] ______________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d141f3400>

    def test_path_instance_on_linux(path_instance):
>       assert isinstance(path_instance._pathlib_home, PurePosixPath)
E       AssertionError: assert False
E        +  where False = isinstance(PureWindowsPath('C:/Users'), PurePosixPath)
E        +    where PureWindowsPath('C:/Users') = <mimesis.providers.path.Path object at 0x7f7d141f3400>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:14: AssertionError
_____________________ test_path_instance_on_darwin[darwin] _____________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d141f3160>

    def test_path_instance_on_darwin(path_instance):
>       assert isinstance(path_instance._pathlib_home, PurePosixPath)
E       AssertionError: assert False
E        +  where False = isinstance(PureWindowsPath('/home'), PurePosixPath)
E        +    where PureWindowsPath('/home') = <mimesis.providers.path.Path object at 0x7f7d141f3160>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:17: AssertionError
_____________________ test_path_instance_on_darwin[win32] ______________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d141f2320>

    def test_path_instance_on_darwin(path_instance):
>       assert isinstance(path_instance._pathlib_home, PurePosixPath)
E       AssertionError: assert False
E        +  where False = isinstance(PureWindowsPath('C:/Users'), PurePosixPath)
E        +    where PureWindowsPath('C:/Users') = <mimesis.providers.path.Path object at 0x7f7d141f2320>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:17: AssertionError
_____________________ test_path_instance_on_darwin[win64] ______________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d141f3730>

    def test_path_instance_on_darwin(path_instance):
>       assert isinstance(path_instance._pathlib_home, PurePosixPath)
E       AssertionError: assert False
E        +  where False = isinstance(PureWindowsPath('C:/Users'), PurePosixPath)
E        +    where PureWindowsPath('C:/Users') = <mimesis.providers.path.Path object at 0x7f7d141f3730>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:17: AssertionError
____________________ test_path_instance_on_windows32[linux] ____________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d1425bbe0>

    def test_path_instance_on_windows32(path_instance):
>       assert isinstance(path_instance._pathlib_home, PureWindowsPath)
E       AssertionError: assert False
E        +  where False = isinstance(PurePosixPath('/home'), PureWindowsPath)
E        +    where PurePosixPath('/home') = <mimesis.providers.path.Path object at 0x7f7d1425bbe0>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:20: AssertionError
____________________ test_path_instance_on_windows64[linux] ____________________

path_instance = <mimesis.providers.path.Path object at 0x7f7d14258b50>

    def test_path_instance_on_windows64(path_instance):
>       assert isinstance(path_instance._pathlib_home, PureWindowsPath)
E       AssertionError: assert False
E        +  where False = isinstance(PurePosixPath('/home'), PureWindowsPath)
E        +    where PurePosixPath('/home') = <mimesis.providers.path.Path object at 0x7f7d14258b50>._pathlib_home

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_linux[darwin]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_linux[win32]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_linux[win64]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_darwin[darwin]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_darwin[win32]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_darwin[win64]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_windows32[linux]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_path_Path_users_folder_1.py::test_path_instance_on_windows64[linux]
========================= 8 failed, 8 passed in 0.13s ==========================
"""