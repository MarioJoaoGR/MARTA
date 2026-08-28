
import pytest
from unittest.mock import patch
from inspect import getsource, getsourcelines, findsource, getfile, getsourcefile
from types import FunctionType
from typing import Callable, Any
import re

# Import the function to be tested
from py_backwards.utils.helpers import get_source


def test_invalid_input():
    with pytest.raises(TypeError):
        get_source(123)

# Add more tests if needed