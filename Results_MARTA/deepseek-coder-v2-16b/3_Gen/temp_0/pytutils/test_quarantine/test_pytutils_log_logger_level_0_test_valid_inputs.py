
import logging
import pytest
from pytutils.log import logger_level

def test_valid_inputs():
    log = logging.getLogger(__name__)
    initial_level = log.level
    
    # Set the logger level to DEBUG within a context block
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.debug('This is a debug message.')  # This should be logged because the level is set to DEBUG
        log.info('This is an info message.')    # This won't be logged because INFO >= DEBUG
    
    # The logger level reverts back to its original setting after the context block
    assert log.level == initial_level
    log.error('This is an error message.')  # This should be logged as it was before the context block

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""