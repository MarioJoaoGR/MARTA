
import pytest
import logging
from pytutils.log import get_logger

def test_no_name():
    log = get_logger()
    assert isinstance(log, logging.Logger)
    log.info('This is an informational message.')

def test_with_name():
    log = get_logger('custom_logger')
    assert isinstance(log, logging.Logger)
    log.info('This is a custom logger message.')
