
import logging
import pytest
from pytutils.log import get_logger  # Assuming this module exists and contains the get_logger function

def test_none_input():
    log = get_logger()
    assert isinstance(log, logging.Logger), "The logger should be an instance of logging.Logger"
    log.info('test')  # This will not raise any errors if the logger is properly configured
