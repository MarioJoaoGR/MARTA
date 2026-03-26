
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

@pytest.mark.parametrize("e, user_msg", [
    (None, None),
    (ValueError('Invalid value'), None),
    (subprocess.CalledProcessError(1, 'cmd', output=b'output'), 'User action required')
])
def test_edge_cases(e, user_msg):
    with patch.object(logger, 'log', side_effect=mock_log):
        log_exception(e, user_msg=user_msg)
