# Module: mimesis.providers.address
import pytest
from mimesis.providers.address import Address

# Test cases for the _dd_to_dms method in the Address class
def test_dd_to_dms_latitude():
    # Test conversion of positive latitude to DMS format
    result = Address._dd_to_dms(40.7128, 'lt')
    assert result == "40º42'46.080\"N"

def test_dd_to_dms_latitude_negative():
    # Test conversion of negative latitude to DMS format
    result = Address._dd_to_dms(-40.7128, 'lt')
    assert result == "40º42'46.080\"S"

def test_dd_to_dms_longitude():
    # Test conversion of positive longitude to DMS format
    result = Address._dd_to_dms(122.43, 'lg')
    assert result == "122º25'48.000\"E"

def test_dd_to_dms_longitude_negative():
    # Test conversion of negative longitude to DMS format
    result = Address._dd_to_dms(-122.43, 'lg')
    assert result == "122º25'48.000\"W"

def test_dd_to_dms_zero():
    # Test conversion of zero latitude or longitude to DMS format
    result = Address._dd_to_dms(0, 'lt')
    assert result == "0º0'0.000\"N"

# Additional edge cases can be added here to ensure robustness and coverage
