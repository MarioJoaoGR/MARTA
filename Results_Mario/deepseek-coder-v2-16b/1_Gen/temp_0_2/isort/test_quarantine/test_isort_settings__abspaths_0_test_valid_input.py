
import os
from typing import Iterable
import pytest

@pytest.fixture(name="_abspaths")
def abspaths():
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
    return _abspaths

@pytest.mark.parametrize("cwd, values, expected", [
    ("home/user", ["folder1/", "file2.txt"], {'home/user/folder1/', 'home/user/file2.txt'}),
    ("/root", ["dir1/", "/file3.txt"], {'/root/dir1/', '/file3.txt'}),
    (".", ["subdir/file1", "file2"], {'./subdir/file1', './file2'}),
])
def test_valid_input(_abspaths, cwd, values, expected):
    assert _abspaths(cwd, values) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input.py F [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
________________ test_valid_input[home/user-values0-expected0] _________________

_abspaths = <function abspaths.<locals>._abspaths at 0x7f28e09df6a0>
cwd = 'home/user', values = ['folder1/', 'file2.txt']
expected = {'home/user/file2.txt', 'home/user/folder1/'}

    @pytest.mark.parametrize("cwd, values, expected", [
        ("home/user", ["folder1/", "file2.txt"], {'home/user/folder1/', 'home/user/file2.txt'}),
        ("/root", ["dir1/", "/file3.txt"], {'/root/dir1/', '/file3.txt'}),
        (".", ["subdir/file1", "file2"], {'./subdir/file1', './file2'}),
    ])
    def test_valid_input(_abspaths, cwd, values, expected):
>       assert _abspaths(cwd, values) == expected
E       AssertionError: assert {'file2.txt',...ser/folder1/'} == {'home/user/f...ser/folder1/'}
E         
E         Extra items in the left set:
E         'file2.txt'
E         Extra items in the right set:
E         'home/user/file2.txt'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input.py:26: AssertionError
____________________ test_valid_input[.-values2-expected2] _____________________

_abspaths = <function abspaths.<locals>._abspaths at 0x7f28e05240e0>, cwd = '.'
values = ['subdir/file1', 'file2'], expected = {'./file2', './subdir/file1'}

    @pytest.mark.parametrize("cwd, values, expected", [
        ("home/user", ["folder1/", "file2.txt"], {'home/user/folder1/', 'home/user/file2.txt'}),
        ("/root", ["dir1/", "/file3.txt"], {'/root/dir1/', '/file3.txt'}),
        (".", ["subdir/file1", "file2"], {'./subdir/file1', './file2'}),
    ])
    def test_valid_input(_abspaths, cwd, values, expected):
>       assert _abspaths(cwd, values) == expected
E       AssertionError: assert {'file2', 'subdir/file1'} == {'./file2', './subdir/file1'}
E         
E         Extra items in the left set:
E         'subdir/file1'
E         'file2'
E         Extra items in the right set:
E         './subdir/file1'
E         './file2'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input.py:26: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input.py::test_valid_input[home/user-values0-expected0]
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input.py::test_valid_input[.-values2-expected2]
========================= 2 failed, 1 passed in 0.07s ==========================
"""