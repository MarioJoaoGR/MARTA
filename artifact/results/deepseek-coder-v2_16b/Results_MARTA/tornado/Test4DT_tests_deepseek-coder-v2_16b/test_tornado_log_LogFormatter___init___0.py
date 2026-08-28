
import pytest
from tornado import log
import logging

def test_default_initialization():
    # Create a logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Initialize LogFormatter with default settings
    formatter = log.LogFormatter()

    # Add a console handler to the logger with the custom formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    # Test logging messages
    assert isinstance(logger, logging.Logger), "Logger should be an instance of logging.Logger"
    logger.debug('A debug message')
    logger.info('An info message')
    logger.warning('A warning message')
    logger.error('An error message')
    logger.critical('A critical message')

def test_custom_format_and_color():
    # Create a logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Initialize LogFormatter with custom format string and color support enabled
    formatter = log.LogFormatter(fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", color=True, colors={logging.DEBUG: 4, logging.INFO: 2})

    # Add a console handler to the logger with the custom formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    # Test logging messages
    assert isinstance(logger, logging.Logger), "Logger should be an instance of logging.Logger"
    formatter.format(logging.LogRecord('my_logger', logging.DEBUG, 'module', 123, 'A debug message', None, None))
    formatter.format(logging.LogRecord('my_logger', logging.INFO, 'module', 123, 'An info message', None, None))
    formatter.format(logging.LogRecord('my_logger', logging.WARNING, 'module', 123, 'A warning message', None, None))
    formatter.format(logging.LogRecord('my_logger', logging.ERROR, 'module', 123, 'An error message', None, None))
    formatter.format(logging.LogRecord('my_logger', logging.CRITICAL, 'module', 123, 'A critical message', None, None))
