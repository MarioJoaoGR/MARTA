
import pytest
import logging
from pytutils.log import configure, DEFAULT_CONFIG

@pytest.fixture(autouse=True)
def setup_logging():
    # Reset logging configuration before each test to ensure a clean state
    logging.root.handlers = []
    logging.root.setLevel(logging.NOTSET)

def test_edge_cases():
    log = logging.getLogger(__name__)
    configure()
    log.info('test')
