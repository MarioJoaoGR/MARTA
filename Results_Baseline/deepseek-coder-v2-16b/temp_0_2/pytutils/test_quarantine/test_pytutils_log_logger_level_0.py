
import logging
import pytest
from pytutils.log import logger_level

# Configure a logger for testing
logger = logging.getLogger(__name__)

def test_logger_level_sets_and_restores_level():
    # Arrange
    initial_level = logger.getEffectiveLevel()
    new_level = logging.DEBUG
    
    # Act
    with logger_level(logger, new_level):
        pass  # Just to trigger the context block execution
    
    # Assert
    assert logger.getEffectiveLevel() == initial_level

def test_logger_level_sets_correct_level():
    # Arrange
    initial_level = logger.getEffectiveLevel()
    new_level = logging.DEBUG
    
    # Act
    with logger_level(logger, new_level):
        assert logger.getEffectiveLevel() == new_level
    
    # Assert
    assert logger.getEffectiveLevel() == initial_level

def test_logger_level_context_manager_restores_original_level():
    # Arrange
    initial_level = logger.getEffectiveLevel()
    new_level = logging.DEBUG
    
    # Act & Assert
    with pytest.raises(AssertionError):  # We expect the level to be different from what it was set to within the context block
        with logger_level(logger, new_level):
            assert logger.getEffectiveLevel() == initial_level
    
    # Assert
    assert logger.getEffectiveLevel() == initial_level
