
import pytest
import re
import typing
from pytutils.env import parse_env_file_contents

def test_default_usage():
    generator = parse_env_file_contents()
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
______________________________ test_default_usage ______________________________

    def test_default_usage():
        generator = parse_env_file_contents()
>       assert list(generator) == []

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

lines = None

    def parse_env_file_contents(lines: typing.Iterable[str] = None) -> typing.Generator[typing.Tuple[str, str], None, None]:
        """
        Parses env file content.
    
        From honcho.
    
        >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
        >>> load_env_file(lines, write_environ=dict())
        OrderedDict([('TEST', '.../yeee'),
                 ('THISIS', '.../a/test'),
                 ('YOLO',
                  '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    
        """
>       for line in lines:
E       TypeError: 'NoneType' object is not iterable

pytutils/pytutils/env.py:27: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0.py::test_default_usage
========================= 1 failed, 1 passed in 0.06s ==========================
"""