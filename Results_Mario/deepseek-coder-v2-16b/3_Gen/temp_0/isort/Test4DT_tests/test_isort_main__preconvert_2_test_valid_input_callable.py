
import pytest
from isort.main import _preconvert
from pathlib import Path
from enum import Enum

def test_valid_input_callable():
    def example_function(): pass
    setattr(example_function, '__name__', 'example_function')
    
    assert _preconvert(example_function) == 'example_function'
