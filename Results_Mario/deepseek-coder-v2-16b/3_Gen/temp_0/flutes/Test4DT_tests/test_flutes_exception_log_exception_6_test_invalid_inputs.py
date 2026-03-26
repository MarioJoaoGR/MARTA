
import pytest
from flutes.exception import log_exception
from unittest.mock import patch
import logging
import traceback
import subprocess

def mock_log(*args, **kwargs):
    pass

logger = logging.getLogger('flutes')
logger.log = lambda *args, **kwargs: mock_log(*args, **kwargs)

@pytest.mark.parametrize("e", [TypeError('Type error'), ValueError('Invalid value')])
def test_invalid_inputs(e):
    with patch('flutes.exception.log', side_effect=mock_log):
        try:
            raise e
        except Exception as exc:
            log_exception(exc)
