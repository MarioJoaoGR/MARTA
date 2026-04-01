
import pytest
from pytutils.log import get_logger
import logging

def test_valid_input_without_name():
    log = get_logger()
    assert isinstance(log, logging.Logger)
    log.info('test')  # This should not raise an error if the logger is correctly configured

def test_valid_input_with_name():
    log = get_logger('test2')
    assert isinstance(log, logging.Logger)
    log.info('test2')  # This should not raise an error if the logger is correctly configured
