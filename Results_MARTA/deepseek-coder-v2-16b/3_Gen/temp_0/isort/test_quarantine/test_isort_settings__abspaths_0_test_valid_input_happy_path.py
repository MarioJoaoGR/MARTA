
import pytest
import os
from typing import Iterable

@pytest.fixture(name="_abspaths")
def abspaths_fixture():
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
    ("home/user", ["folder1/", "file1.txt"], {'home/user/folder1/', 'file1.txt'}),
    ("/root", ["subdir/file2.txt", "/absolute/path"], {'/root/subdir/file2.txt', '/absolute/path'}),
    ("home/user", ["folder1/", "file1.txt", "another_folder/"], {'home/user/folder1/', 'home/user/file1.txt', 'home/user/another_folder/'}),
    ("/root", ["subdir/file2.txt", "/absolute/path", "another_subdir/file3.txt"], {'/root/subdir/file2.txt', '/absolute/path', '/root/another_subdir/file3.txt'}),
])
def test_valid_input_happy_path(_abspaths, cwd, values, expected):
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
collected 4 items

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input_happy_path.py . [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________ test_valid_input_happy_path[/root-values1-expected1] _____________

_abspaths = <function abspaths_fixture.<locals>._abspaths at 0x7f4303a5f560>
cwd = '/root', values = ['subdir/file2.txt', '/absolute/path']
expected = {'/absolute/path', '/root/subdir/file2.txt'}

    @pytest.mark.parametrize("cwd, values, expected", [
        ("home/user", ["folder1/", "file1.txt"], {'home/user/folder1/', 'file1.txt'}),
        ("/root", ["subdir/file2.txt", "/absolute/path"], {'/root/subdir/file2.txt', '/absolute/path'}),
        ("home/user", ["folder1/", "file1.txt", "another_folder/"], {'home/user/folder1/', 'home/user/file1.txt', 'home/user/another_folder/'}),
        ("/root", ["subdir/file2.txt", "/absolute/path", "another_subdir/file3.txt"], {'/root/subdir/file2.txt', '/absolute/path', '/root/another_subdir/file3.txt'}),
    ])
    def test_valid_input_happy_path(_abspaths, cwd, values, expected):
        result = _abspaths(cwd, values)
>       assert result == expected
E       AssertionError: assert {'/absolute/p...ir/file2.txt'} == {'/absolute/p...ir/file2.txt'}
E         
E         Extra items in the left set:
E         'subdir/file2.txt'
E         Extra items in the right set:
E         '/root/subdir/file2.txt'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input_happy_path.py:28: AssertionError
___________ test_valid_input_happy_path[home/user-values2-expected2] ___________

_abspaths = <function abspaths_fixture.<locals>._abspaths at 0x7f4303a5fec0>
cwd = 'home/user', values = ['folder1/', 'file1.txt', 'another_folder/']
expected = {'home/user/another_folder/', 'home/user/file1.txt', 'home/user/folder1/'}

    @pytest.mark.parametrize("cwd, values, expected", [
        ("home/user", ["folder1/", "file1.txt"], {'home/user/folder1/', 'file1.txt'}),
        ("/root", ["subdir/file2.txt", "/absolute/path"], {'/root/subdir/file2.txt', '/absolute/path'}),
        ("home/user", ["folder1/", "file1.txt", "another_folder/"], {'home/user/folder1/', 'home/user/file1.txt', 'home/user/another_folder/'}),
        ("/root", ["subdir/file2.txt", "/absolute/path", "another_subdir/file3.txt"], {'/root/subdir/file2.txt', '/absolute/path', '/root/another_subdir/file3.txt'}),
    ])
    def test_valid_input_happy_path(_abspaths, cwd, values, expected):
        result = _abspaths(cwd, values)
>       assert result == expected
E       AssertionError: assert {'file1.txt',...ser/folder1/'} == {'home/user/a...ser/folder1/'}
E         
E         Extra items in the left set:
E         'file1.txt'
E         Extra items in the right set:
E         'home/user/file1.txt'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input_happy_path.py:28: AssertionError
_____________ test_valid_input_happy_path[/root-values3-expected3] _____________

_abspaths = <function abspaths_fixture.<locals>._abspaths at 0x7f4303a01120>
cwd = '/root'
values = ['subdir/file2.txt', '/absolute/path', 'another_subdir/file3.txt']
expected = {'/absolute/path', '/root/another_subdir/file3.txt', '/root/subdir/file2.txt'}

    @pytest.mark.parametrize("cwd, values, expected", [
        ("home/user", ["folder1/", "file1.txt"], {'home/user/folder1/', 'file1.txt'}),
        ("/root", ["subdir/file2.txt", "/absolute/path"], {'/root/subdir/file2.txt', '/absolute/path'}),
        ("home/user", ["folder1/", "file1.txt", "another_folder/"], {'home/user/folder1/', 'home/user/file1.txt', 'home/user/another_folder/'}),
        ("/root", ["subdir/file2.txt", "/absolute/path", "another_subdir/file3.txt"], {'/root/subdir/file2.txt', '/absolute/path', '/root/another_subdir/file3.txt'}),
    ])
    def test_valid_input_happy_path(_abspaths, cwd, values, expected):
        result = _abspaths(cwd, values)
>       assert result == expected
E       AssertionError: assert {'/absolute/p...ir/file2.txt'} == {'/absolute/p...ir/file2.txt'}
E         
E         Extra items in the left set:
E         'another_subdir/file3.txt'
E         'subdir/file2.txt'
E         Extra items in the right set:
E         '/root/subdir/file2.txt'
E         '/root/another_subdir/file3.txt'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input_happy_path.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input_happy_path.py::test_valid_input_happy_path[/root-values1-expected1]
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input_happy_path.py::test_valid_input_happy_path[home/user-values2-expected2]
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0_test_valid_input_happy_path.py::test_valid_input_happy_path[/root-values3-expected3]
========================= 3 failed, 1 passed in 0.10s ==========================
"""