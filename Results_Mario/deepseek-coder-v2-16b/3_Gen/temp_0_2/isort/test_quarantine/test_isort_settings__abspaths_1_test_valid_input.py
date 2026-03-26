
import os
from typing import Iterable

def _abspaths(cwd: str, values: Iterable[str]) -> set[str]:
    paths = {
        (
            os.path.join(cwd, value)
            if not value.startswith(os.path.sep) and value.endswith(os.path.sep)
            else value
        )
        for value in values
    }
    return paths

import pytest
from unittest.mock import patch

@pytest.mark.parametrize("cwd, values, expected", [
    ("home/user", ["folder1/", "file2.txt"], {"home/user/folder1/", "file2.txt"}),
    ("/root", ["dir1/", "/file3.txt"], {"/root/dir1/", "/file3.txt"}),
])
def test_valid_input(cwd, values, expected):
    with patch('os.path.join', side_effect=lambda cwd, value: os.path.join(cwd, value)):
        result = _abspaths(cwd, values)
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________ test_valid_input[home/user-values0-expected0] _________________

cwd = 'home/user', values = ['folder1/', 'file2.txt']
expected = {'file2.txt', 'home/user/folder1/'}

    @pytest.mark.parametrize("cwd, values, expected", [
        ("home/user", ["folder1/", "file2.txt"], {"home/user/folder1/", "file2.txt"}),
        ("/root", ["dir1/", "/file3.txt"], {"/root/dir1/", "/file3.txt"}),
    ])
    def test_valid_input(cwd, values, expected):
        with patch('os.path.join', side_effect=lambda cwd, value: os.path.join(cwd, value)):
>           result = _abspaths(cwd, values)

isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:6: in _abspaths
    paths = {
isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:8: in <setcomp>
    os.path.join(cwd, value)
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:24: in <lambda>
    with patch('os.path.join', side_effect=lambda cwd, value: os.path.join(cwd, value)):
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded while calling a Python object
!!! Recursion detected (same locals & position)
__________________ test_valid_input[/root-values1-expected1] ___________________

cwd = '/root', values = ['dir1/', '/file3.txt']
expected = {'/file3.txt', '/root/dir1/'}

    @pytest.mark.parametrize("cwd, values, expected", [
        ("home/user", ["folder1/", "file2.txt"], {"home/user/folder1/", "file2.txt"}),
        ("/root", ["dir1/", "/file3.txt"], {"/root/dir1/", "/file3.txt"}),
    ])
    def test_valid_input(cwd, values, expected):
        with patch('os.path.join', side_effect=lambda cwd, value: os.path.join(cwd, value)):
>           result = _abspaths(cwd, values)

isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:6: in _abspaths
    paths = {
isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:8: in <setcomp>
    os.path.join(cwd, value)
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py:24: in <lambda>
    with patch('os.path.join', side_effect=lambda cwd, value: os.path.join(cwd, value)):
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded while calling a Python object
!!! Recursion detected (same locals & position)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py::test_valid_input[home/user-values0-expected0]
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_1_test_valid_input.py::test_valid_input[/root-values1-expected1]
============================== 2 failed in 0.24s ===============================
"""