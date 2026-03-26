
import os
import pytest
from unittest.mock import patch

def expand(val: str) -> str:
    val = os.path.expandvars(val)
    val = os.path.expanduser(val)
    return val

@pytest.fixture(autouse=True)
def mock_env_variables():
    with patch.dict(os.environ, {'USER': 'admin', 'HOME': '/root'}):
        yield

def test_valid_input():
    assert expand("~/Documents") == "/home/user/Documents"
    assert expand("$USER/Desktop") == "admin/Desktop"
    assert expand("~") == "/home/user"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""