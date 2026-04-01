
import pytest
from dataclasses_json.core import _ExtendedEncoder

def test_invalid_inputs():
    encoder = _ExtendedEncoder()
    
    # Test invalid input types
    with pytest.raises(TypeError):
        encoder.default(None)  # None is not a valid type for this encoder
