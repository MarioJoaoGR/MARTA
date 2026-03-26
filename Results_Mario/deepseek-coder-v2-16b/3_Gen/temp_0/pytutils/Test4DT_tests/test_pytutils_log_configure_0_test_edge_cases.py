
import pytest
from pytutils.log import configure, DEFAULT_CONFIG, get_config
import logging

@pytest.fixture(autouse=True)
def setup_logging():
    # Reset logging configuration before each test
    logging.root.setLevel(logging.NOTSET)
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)

def test_edge_cases():
    log = logging.getLogger(__name__)
    configure()
    log.info('test')
