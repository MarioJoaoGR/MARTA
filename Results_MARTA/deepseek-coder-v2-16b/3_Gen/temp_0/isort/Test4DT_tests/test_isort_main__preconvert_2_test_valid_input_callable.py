
from enum import Enum
from pathlib import Path

import pytest

from isort.main import _preconvert


def test_valid_input_callable():
    def example_function(): pass
    setattr(example_function, '__name__', 'example_function')
    
    assert _preconvert(example_function) == 'example_function'
