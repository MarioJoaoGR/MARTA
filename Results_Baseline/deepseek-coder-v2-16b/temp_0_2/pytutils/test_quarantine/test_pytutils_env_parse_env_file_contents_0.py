
import pytest
import re
import typing
from pytutils.env import parse_env_file_contents

# Test cases for parse_env_file_contents function

def test_parse_env_file_contents_with_list():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed_lines = list(parse_env_file_contents(lines))
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0.py F. [100%]

=================================== FAILURES ===================================
____________________ test_parse_env_file_contents_with_list ____________________

    def test_parse_env_file_contents_with_list():
        lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
        parsed_lines = list(parse_env_file_contents(lines))
>       assert parsed_lines == [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
E       AssertionError: assert [('TEST', '${...S_NOT_EXIST')] == [('TEST', '.....S_NOT_EXIST')]
E         
E         At index 0 diff: ('TEST', '${HOME}/yeee') != ('TEST', '.../yeee')
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0.py::test_parse_env_file_contents_with_list
========================= 1 failed, 1 passed in 0.06s ==========================
"""