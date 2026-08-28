
import pytest
import time
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import strftime

# Test cases for the strftime function
def test_strftime_with_format():
    # Test with a specific format string
    result = strftime("%Y-%m-%d %H:%M:%S", 1696488000)
    assert isinstance(result, str), "Expected a string output"
    assert result == '2023-10-05 14:30:00', f"Unexpected result for format '%Y-%m-%d %H:%M:%S': {result}"

def test_strftime_default_format():
    # Test without providing a format string, should default to '%Y-%m-%d'
    current_time = time.localtime(1696488000)  # Convert epoch seconds to local time
    result = strftime('%Y-%m-%d', current_time)
    assert isinstance(result, str), "Expected a string output"
    expected_default_format = time.strftime('%Y-%m-%d', current_time)
    assert result == expected_default_format, f"Unexpected default format result: {result}"

def test_strftime_invalid_epoch():
    # Test with an invalid epoch value that should raise AnsibleFilterError
    with pytest.raises(AnsibleFilterError) as excinfo:
        strftime("%Y-%m-%d %H:%M:%S", "invalid_value")
    assert str(excinfo.value) == 'Invalid value for epoch value (invalid_value)', "Expected an error message indicating invalid epoch value"

def test_strftime_nonexistent_format():
    # Test with a format string that does not exist, should raise a ValueError from time.strftime
    with pytest.raises(ValueError) as excinfo:
        strftime("This is not a valid format", 1696488000)
    assert str(excinfo.value).startswith('time data does not match format'), "Expected a ValueError indicating the format is invalid"
