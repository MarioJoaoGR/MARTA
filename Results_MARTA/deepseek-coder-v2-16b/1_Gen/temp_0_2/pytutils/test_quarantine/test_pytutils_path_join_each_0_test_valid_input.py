
import os
from pytutils.path import join_each
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("parent, iterable, expected", [
    ("/home/user", ["file1", "file2"], ["/home/user/file1", "/home/user/file2"]),
    ("/home/user/", ["file1", "file2"], ["/home/user/file1", "/home/user/file2"]),
    ("/home/user", ["dir1/file1", "dir2/file2"], ["/home/user/dir1/file1", "/home/user/dir2/file2"])
])
@patch('os.path.join')
def test_valid_input(mock_join, parent, iterable, expected):
    mock_join.side_effect = lambda x, y: f"{x}/{y}"
    
    result = list(join_each(parent, iterable))
    
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_path_join_each_0_test_valid_input.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
______________ test_valid_input[/home/user/-iterable1-expected1] _______________

mock_join = <MagicMock name='join' id='140328156855952'>, parent = '/home/user/'
iterable = ['file1', 'file2']
expected = ['/home/user/file1', '/home/user/file2']

    @pytest.mark.parametrize("parent, iterable, expected", [
        ("/home/user", ["file1", "file2"], ["/home/user/file1", "/home/user/file2"]),
        ("/home/user/", ["file1", "file2"], ["/home/user/file1", "/home/user/file2"]),
        ("/home/user", ["dir1/file1", "dir2/file2"], ["/home/user/dir1/file1", "/home/user/dir2/file2"])
    ])
    @patch('os.path.join')
    def test_valid_input(mock_join, parent, iterable, expected):
        mock_join.side_effect = lambda x, y: f"{x}/{y}"
    
        result = list(join_each(parent, iterable))
    
>       assert result == expected
E       AssertionError: assert ['/home/user/.../user//file2'] == ['/home/user/...e/user/file2']
E         
E         At index 0 diff: '/home/user//file1' != '/home/user/file1'
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_path_join_each_0_test_valid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_path_join_each_0_test_valid_input.py::test_valid_input[/home/user/-iterable1-expected1]
========================= 1 failed, 2 passed in 0.05s ==========================
"""