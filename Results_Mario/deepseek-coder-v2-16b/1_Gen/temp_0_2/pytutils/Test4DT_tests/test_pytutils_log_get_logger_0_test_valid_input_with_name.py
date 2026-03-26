
import pytest
import logging
from pytutils.log import get_logger, _ensure_configured, _namespace_from_calling_context

@pytest.fixture(autouse=True)
def setup():
    # Ensure the logger is properly configured for testing
    _ensure_configured()

def test_valid_input_with_name():
    log = get_logger('test2')
    assert isinstance(log, logging.Logger), "Expected a logger instance"
    log.info('test2')  # This should not raise an exception if the logger is correctly configured
