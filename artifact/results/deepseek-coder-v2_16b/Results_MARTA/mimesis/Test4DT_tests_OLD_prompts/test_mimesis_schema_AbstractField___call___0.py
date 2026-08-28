
import pytest
from unittest.mock import patch, MagicMock
from mimesis.schema import AbstractField
from mimesis.exceptions import UnsupportedField

# Test scenario 1: Valid inputs should return a valid result

# Test scenario 2: Invalid name should raise UnsupportedField error
def test_invalid_name():
    field = AbstractField(locale='en')
    
    with patch('mimesis.Generic', autospec=True) as mock_generic:
        mock_provider = MagicMock()
        mock_generic.return_value._gen = mock_provider
        
        with pytest.raises(UnsupportedField):
            field('invalid_name')

# Test scenario 3: Providing a key function should apply it to the result