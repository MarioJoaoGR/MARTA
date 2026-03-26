
import os
import collections
import typing
import pytest
from pytutils.env import load_env_file

@pytest.fixture
def example_lines():
    return ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

def test_load_env_file(example_lines):
    result = load_env_file(example_lines, write_environ=dict())
    expected = collections.OrderedDict([('TEST', os.path.expanduser('${HOME}/yeee-$PATH')), 
                                         ('THISIS', os.path.expanduser('~/a/test')), 
                                         ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])
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

pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0.py F.           [100%]

=================================== FAILURES ===================================
______________________________ test_load_env_file ______________________________

example_lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    def test_load_env_file(example_lines):
        result = load_env_file(example_lines, write_environ=dict())
        expected = collections.OrderedDict([('TEST', os.path.expanduser('${HOME}/yeee-$PATH')),
                                             ('THISIS', os.path.expanduser('~/a/test')),
                                             ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected OrderedDict([('TEST', '${HOME}/yeee-$PATH'), ('THISIS', '/home/joaovitorino/a/test'), ('YOLO', '/home/joaovitorino/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]), but got OrderedDict([('TEST', '/home/joaovitorino/yeee-/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'), ('THISIS', '/home/joaovitorino/a/test'), ('YOLO', '/home/joaovitorino/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
E       assert OrderedDict([..._NOT_EXIST')]) == OrderedDict([..._NOT_EXIST')])
E         
E         Omitting 2 identical items, use -vv to show
E         Differing items:
E         {'TEST': '/home/joaovitorino/yeee-/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'} != {'TEST': '${HOME}/yeee-$PATH'}
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0.py::test_load_env_file
========================= 1 failed, 1 passed in 0.08s ==========================
"""