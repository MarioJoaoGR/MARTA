
import pytest
from pytutils.log import configure, DEFAULT_CONFIG
import logging

@pytest.fixture(autouse=True)
def setup_logging():
    # Reset logging configuration before each test
    logging.config.dictConfig({})

def test_invalid_inputs():
    with pytest.raises(Exception):
        configure({'invalid': 'config'})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""