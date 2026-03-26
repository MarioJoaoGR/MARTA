
import os
import pytest
from pytutils.log import get_config

@pytest.fixture(autouse=True)
def unset_env_var():
    if 'LOG_CONFIG' in os.environ:
        del os.environ['LOG_CONFIG']

def test_missing_env_var():
    with pytest.raises(ValueError):
        get_config(env_var='LOG_CONFIG', default={'default': 'config'})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""