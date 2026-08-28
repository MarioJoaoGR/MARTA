
import pytest
from unittest.mock import patch
import logging
from tornado.log import enable_pretty_logging
import tornado.options



def test_enable_pretty_logging_with_options():
    """Test using parsed command line options in enable_pretty_logging."""
    class Options:
        logging = 'info'
        log_file_prefix = None
        log_to_stderr = True
        # Add other necessary options here if needed for testing
    
    with patch('tornado.options.parse_command_line', return_value=Options()):
        enable_pretty_logging(options=Options())
        assert logging.getLogger().level == logging.INFO

