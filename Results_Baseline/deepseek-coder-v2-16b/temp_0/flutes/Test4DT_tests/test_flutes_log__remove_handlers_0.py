# Module: flutes.log
import logging
import pytest
from flutes.log import _remove_handlers

# Test fixture to create a logger with handlers for each test
@pytest.fixture
def setup_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    handler1 = logging.FileHandler('file1.log')
    logger.addHandler(handler1)
    
    handler2 = logging.StreamHandler()
    logger.addHandler(handler2)
    
    yield logger
    
    # Teardown: Remove all handlers from the logger
    _remove_handlers(logger)

def test_remove_handlers_no_handlers(setup_logger):
    logger = setup_logger
    initial_handlers_count = len(logger.handlers)
    assert initial_handlers_count == 2, f"Expected 2 handlers but found {initial_handlers_count}"
    
    _remove_handlers(logger)
    final_handlers_count = len(logger.handlers)
    assert final_handlers_count == 0, f"Expected 0 handlers but found {final_handlers_count}"

def test_remove_handlers_multiple_handlers(setup_logger):
    logger = setup_logger
    initial_handlers_count = len(logger.handlers)
    assert initial_handlers_count == 2, f"Expected 2 handlers but found {initial_handlers_count}"
    
    _remove_handlers(logger)
    final_handlers_count = len(logger.handlers)
    assert final_handlers_count == 0, f"Expected 0 handlers but found {final_handlers_count}"

def test_remove_handlers_one_handler(setup_logger):
    logger = setup_logger
    initial_handlers_count = len(logger.handlers)
    assert initial_handlers_count == 2, f"Expected 2 handlers but found {initial_handlers_count}"
    
    _remove_handlers(logger)
    final_handlers_count = len(logger.handlers)
    assert final_handlers_count == 0, f"Expected 0 handlers but found {final_handlers_count}"
