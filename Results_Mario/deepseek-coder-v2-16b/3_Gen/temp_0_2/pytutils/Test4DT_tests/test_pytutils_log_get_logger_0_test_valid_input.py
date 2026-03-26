
import pytest
import logging
from pytutils.log import get_logger

def test_valid_input():
    log = get_logger()
    assert isinstance(log, logging.Logger)
    
    log2 = get_logger('test2')
    assert isinstance(log2, logging.Logger)
