
import pytest
from unittest.mock import patch, MagicMock
from mimesis.builtins.en import USASpecProvider

# Test for valid input - USPS

# Test for valid input - FedEx

# Test for valid input - UPS

# Test for invalid input - Unsupported service
def test_invalid_input():
    provider = USASpecProvider()
    with pytest.raises(ValueError):
        provider.tracking_number('dhl')