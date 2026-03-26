
import pytest
from flutes.log import get_logging_levels
from typing import List
import logging

# Define a dummy LoggingLevel for the purpose of this test
class LoggingLevel(int):
    pass

# Mock LEVEL_MAP to simulate the available logging levels
LEVEL_MAP = {
    'DEBUG': LoggingLevel(10),
    'INFO': LoggingLevel(20),
    'WARNING': LoggingLevel(30),
    'ERROR': LoggingLevel(40),
    'CRITICAL': LoggingLevel(50)
}

def test_get_logging_levels():
    logging_levels = get_logging_levels()
    expected_levels = [LoggingLevel(10), LoggingLevel(20), LoggingLevel(30), LoggingLevel(40), LoggingLevel(50)]
    
    assert isinstance(logging_levels, list)