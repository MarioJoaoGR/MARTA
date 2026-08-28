
import pytest
import datetime

def to_datetime(string, format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strptime(string, format)

# Test valid input with default format
def test_valid_input_default_format():
    string = '2023-04-15 12:30:00'
    expected_output = datetime.datetime(2023, 4, 15, 12, 30, 0)
    assert to_datetime(string) == expected_output

# Test valid input with custom format
def test_valid_input_custom_format():
    string = '15/04/2023 12:30:00'
    format = '%d/%m/%Y %H:%M:%S'
    expected_output = datetime.datetime(2023, 4, 15, 12, 30, 0)
    assert to_datetime(string, format) == expected_output

# Test invalid input that raises ValueError
def test_invalid_input():
    string = 'InvalidDate'
    format = '%Y-%m-%d %H:%M:%S'
    with pytest.raises(ValueError):
        to_datetime(string, format)
