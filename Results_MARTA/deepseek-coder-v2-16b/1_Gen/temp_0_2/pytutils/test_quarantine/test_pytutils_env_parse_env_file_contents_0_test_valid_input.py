
import pytest
from pytutils.env import parse_env_file_contents
import os
import re
import typing

@pytest.mark.parametrize("lines", [['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']])
def test_valid_input(lines):
    expected_output = [('TEST', os.path.expanduser('${HOME}/yeee')), ('THISIS', os.path.expanduser('~/a/test')), ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]
    parsed_lines = list(parse_env_file_contents(lines))
    assert parsed_lines == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_valid_input[lines0] ___________________________

lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    @pytest.mark.parametrize("lines", [['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']])
    def test_valid_input(lines):
        expected_output = [('TEST', os.path.expanduser('${HOME}/yeee')), ('THISIS', os.path.expanduser('~/a/test')), ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]
        parsed_lines = list(parse_env_file_contents(lines))
>       assert parsed_lines == expected_output
E       AssertionError: assert [('TEST', '${...S_NOT_EXIST')] == [('TEST', '${...S_NOT_EXIST')]
E         
E         At index 1 diff: ('THISIS', '~/a/test') != ('THISIS', '/home/joaovitorino/a/test')
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0_test_valid_input.py::test_valid_input[lines0]
============================== 1 failed in 0.05s ===============================
"""