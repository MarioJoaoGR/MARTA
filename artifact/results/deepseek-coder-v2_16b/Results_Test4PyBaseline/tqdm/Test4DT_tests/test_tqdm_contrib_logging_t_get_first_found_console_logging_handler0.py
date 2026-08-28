# Module: tqdm.contrib.logging
import logging
import sys
from tqdm.contrib.logging import _get_first_found_console_logging_handler, _is_console_logging_handler

def test__get_first_found_console_logging_handler():
    # Create some logging handlers
    handler1 = logging.StreamHandler(sys.stdout)
    handler2 = logging.FileHandler('example.log')
    
    # List of handlers to check
    handlers_list = [handler1, handler2]
    
    # Get the first found console logging handler
    console_handler = _get_first_found_console_logging_handler(handlers_list)
    
    assert isinstance(console_handler, logging.StreamHandler), "Expected a StreamHandler"
    assert console_handler.stream == sys.stdout, "Expected the stream to be sys.stdout"

def test__is_console_logging_handler():
    # Create a StreamHandler for stdout and check if it is a console handler
    handler = logging.StreamHandler(sys.stdout)
    
    assert _is_console_logging_handler(handler), "Expected the handler to be identified as a console handler"

def test__get_first_found_console_logging_handler_no_handlers():
    # Test with an empty list of handlers
    handlers_list = []
    
    assert _get_first_found_console_logging_handler(handlers_list) is None, "Expected None when no handlers are provided"

def test__get_first_found_console_logging_handler_no_console_handlers():
    # Create a FileHandler and check that it does not qualify as a console handler
    handler = logging.FileHandler('example.log')
    
    assert not _is_console_logging_handler(handler), "Expected the handler to be identified as not a console handler"
    
    handlers_list = [handler]
    console_handler = _get_first_found_console_logging_handler(handlers_list)
    
    assert console_handler is None, "Expected None when no console handlers are found"
