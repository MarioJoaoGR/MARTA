
import pytest
import logging
from pytutils.log import configure, DEFAULT_CONFIG, get_config

@pytest.fixture(autouse=True)
def setup_logging():
    # Reset logging configurations before each test
    logging.root.setLevel(logging.NOTSET)
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        configure({'invalid': 'config'})
