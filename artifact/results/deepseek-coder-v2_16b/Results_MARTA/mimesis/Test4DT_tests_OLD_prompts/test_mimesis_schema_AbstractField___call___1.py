
import pytest
from unittest.mock import MagicMock, patch
from mimesis.schema import AbstractField
from mimesis.exceptions import UndefinedField, UnsupportedField



def test_invalid_inputs_with_kwargs():
    with patch('mimesis.Generic') as mock_generic:
        mock_instance = MagicMock()
        mock_generic.return_value = mock_instance

        field = AbstractField(locale='en')
        
        # Test method with invalid kwargs
        with pytest.raises(UnsupportedField):
            field('person', first_name=True, invalid_kwarg=True)