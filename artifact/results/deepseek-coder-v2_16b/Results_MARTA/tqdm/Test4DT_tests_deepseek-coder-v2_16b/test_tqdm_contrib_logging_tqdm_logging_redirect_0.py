
import pytest
from tqdm.contrib.logging import tqdm_logging_redirect
import logging
from tqdm import trange

# Set up a logger
LOG = logging.getLogger(__name__)


def test_tqdm_logging_redirect_with_default_tqdm():
    """Test usage of tqdm_logging_redirect with the default TQDM class."""
    with tqdm_logging_redirect() as pbar:
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        assert pbar is not None, "Progress bar should be created and managed by tqdm_logging_redirect."

def test_tqdm_logging_redirect_with_custom_tqdm():
    """Test usage of tqdm_logging_redirect with a custom TQDM class."""
    from tqdm import tqdm as CustomTQDM
    with tqdm_logging_redirect(tqdm_class=CustomTQDM) as pbar:
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        assert isinstance(pbar, CustomTQDM), "Progress bar should be an instance of the custom TQDM class."

def test_tqdm_logging_redirect_with_specified_loggers():
    """Test usage of tqdm_logging_redirect with specified loggers."""
    logger1 = logging.getLogger('logger1')
    logger2 = logging.getLogger('logger2')
    with tqdm_logging_redirect(loggers=[logger1, logger2]) as pbar:
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
        assert pbar is not None, "Progress bar should be created and managed by tqdm_logging_redirect."