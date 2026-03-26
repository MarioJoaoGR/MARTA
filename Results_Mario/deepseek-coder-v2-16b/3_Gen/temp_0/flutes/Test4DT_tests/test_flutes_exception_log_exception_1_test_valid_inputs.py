
import pytest
from flutes.exception import log_exception
from unittest.mock import patch
import logging
import traceback
import subprocess

logger = logging.getLogger('flutes')
def mock_log(*args, **kwargs): pass
logger.log = lambda *args, **kwargs: mock_log(*args, **kwargs)

@pytest.fixture(autouse=True)
def setup():
    yield  # Ensure the test runs after setting up the mock

def test_valid_inputs():
    with patch('flutes.exception.log', side_effect=mock_log):
        try:
            log_exception(ValueError('Invalid value'), user_msg='User action required')
        except ValueError as e:
            assert str(e) == 'Invalid value'
            assert "User action required" in logger.handlers[0].buffer.getvalue().decode()
