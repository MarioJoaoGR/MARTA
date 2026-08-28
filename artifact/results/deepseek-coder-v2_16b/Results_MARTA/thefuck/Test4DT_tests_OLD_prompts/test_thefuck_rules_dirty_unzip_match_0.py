
import pytest
from unittest.mock import patch, MagicMock
from thefuck.rules.dirty_unzip import match



def test_invalid_input_none():
    command = None
    with pytest.raises(AttributeError):
        match(command)