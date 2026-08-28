
import pytest
import logging
from tornado.log import enable_pretty_logging
from tornado.options import OptionParser

def test_enable_pretty_logging_custom_logger():
    logger = logging.getLogger('my_logger')
    enable_pretty_logging(logger=logger)
    assert len(logger.handlers) == 1, "Expected one handler to be added to the custom logger"

class TestOptions:
    def __init__(self):
        self.logging = "info"
        self.log_file_prefix = None
        self.log_to_stderr = True
        self.log_rotate_mode = "size"
        self.log_file_max_size = 1024 * 1024  # 1MB
        self.log_file_num_backups = 5

