
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Left().to_validation()
