
import pytest
from unittest.mock import patch, MagicMock
import logging
import multiprocessing as mp
from pathlib import Path
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield logger
    # Teardown: remove the handler to avoid affecting other tests
    logger.removeHandler(handler)

def test_send_none(logger):
    with patch('flutes.log.mp', autospec=True) as mock_mp:
        mock_queue = MagicMock()
        mock_mp.Queue.return_value = mock_queue
        logger.handlers[0].send(None)
        assert not mock_queue.put_nowait.called, "Expected no call to put_nowait with None"
