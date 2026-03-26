
import os
import logging
import pytest
from pytutils.log import configure, DEFAULT_CONFIG

@pytest.fixture(autouse=True)
def setup():
    # Set up the environment variable for testing
    os.environ['LOGGING'] = '{"version": 1, "disable_existing_loggers": false, "handlers": [{"type": "console"}]}'
    logging.setLoggerClass(logging.getLoggerClass())  # Ensure we can set a logger in the test

@pytest.mark.skipif(not os.getenv('LOGGING'), reason="LOGGING environment variable not set")
def test_valid_inputs():
    configure()
    log = logging.getLogger(__name__)
    log.info('test')  # Check if this logs with the configured settings
