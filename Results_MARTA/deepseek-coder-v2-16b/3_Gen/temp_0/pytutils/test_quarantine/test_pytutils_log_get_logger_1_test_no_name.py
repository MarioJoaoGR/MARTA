
import logging
from pytutils.log import get_logger
import pytest

def test_no_name():
    # Ensure no exception is raised when getting a logger without a name
    log = get_logger()
    
    # Check if the logger was created with a default name derived from the calling context
    assert isinstance(log, logging.Logger)
