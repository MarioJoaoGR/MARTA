
import pytest
from tqdm.contrib.logging import logging_redirect_tqdm
from tqdm import tqdm as std_tqdm
import logging
import time

# Set up a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@pytest.fixture
def setup_logger():
    logger1 = logging.getLogger('logger1')
    logger1.setLevel(logging.INFO)
    logger2 = logging.getLogger('logger2')
    logger2.setLevel(logging.INFO)
    return logger1, logger2

def test_default_usage():
    with logging_redirect_tqdm() as pbar:
        for i in range(10):
            if i == 5:
                logger.info("Console logging redirected to `tqdm.write()`")
            time.sleep(0.1)
        assert True, "Test should not raise any errors"

def test_custom_progress_bar():
    from tqdm import tqdm as custom_tqdm
    with logging_redirect_tqdm(tqdm_class=custom_tqdm) as pbar:
        for i in range(10):
            if i == 5:
                logger.info("Console logging redirected to `custom_tqdm.write()`")
            time.sleep(0.1)
        assert True, "Test should not raise any errors"

def test_specifying_loggers(setup_logger):
    logger1, logger2 = setup_logger
    with logging_redirect_tqdm([logger1, logger2]) as pbar:
        for i in range(10):
            if i == 5:
                logger1.info("Console logging redirected to `tqdm.write()`")
                logger2.info("Console logging redirected to `tqdm.write()`")
            time.sleep(0.1)