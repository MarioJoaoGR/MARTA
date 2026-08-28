
import pytest
from unittest.mock import patch, MagicMock
from pymonet.validation import Validation
from pymonet.box import Box

def test_valid_input():
    validation = Validation(value=42, errors=[])
    box = validation.to_box()
    assert isinstance(box, Box)
    assert box.value == 42
