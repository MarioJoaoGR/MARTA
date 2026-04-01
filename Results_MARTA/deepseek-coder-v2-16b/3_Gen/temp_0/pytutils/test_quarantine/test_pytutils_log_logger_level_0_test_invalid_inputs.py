
import pytest
from pytutils.log import logger_level
import logging

def test_logger_level():
    # Create a mock logger
    log = logging.getLogger("test")
    
    # Set the initial level to DEBUG
    assert log.level == logging.DEBUG
    
    # Change the logger level within the context block
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
        
        # Log messages at different levels
        log.debug('This is a debug message.')  # This won't be logged because INFO < DEBUG
        log.info('This is an info message.')    # This will be logged because INFO >= INFO
        log.error('This is an error message.')  # This will be logged as it was before the context block
    
    # Check that the logger level has reverted back to its original setting
    assert log.level == logging.DEBUG

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""