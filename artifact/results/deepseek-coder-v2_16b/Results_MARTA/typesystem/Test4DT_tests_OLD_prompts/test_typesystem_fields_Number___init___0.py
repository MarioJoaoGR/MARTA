
import pytest
from unittest.mock import patch
from typesystem.fields import Number



def test_invalid_inputs():
    with pytest.raises(AssertionError):
        Number(minimum='not an int', maximum=10, exclusive_minimum=5, multiple_of=2)