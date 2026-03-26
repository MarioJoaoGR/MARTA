
from datetime import timedelta, timezone
import pytest

# Assuming the function definition and its docstring are correct as provided
def cached_tz(hour_str: str, minute_str: str, sign_str: str) -> timezone:
    """
    Generate a timezone object based on the provided hour, minute, and sign strings.

    Parameters:
        hour_str (str): A string representing the hour component of the timezone offset.
            This should be an integer value.
        minute_str (str): A string representing the minute component of the timezone offset.
            This should be an integer value.
        sign_str (str): A string indicating the sign of the timezone offset, either "+" or "-".

    Returns:
        timezone: A Python `timezone` object representing the specified timezone offset.

    Examples:
        >>> cached_tz("1", "30", "+")
        <UTC+01:30>
        
        >>> cached_tz("2", "45", "-")
        <UTC-02:45>
        
        >>> cached_tz("0", "0", "+")
        <UTC+00:00>
    
    Notes:
        - The `hour_str` and `minute_str` parameters are expected to be valid integers.
        - The `sign_str` parameter should be either "+" or "-".
        - This function constructs a timezone object using the provided offset, which can then be used in datetime operations.
    """
    sign = 1 if sign_str == "+" else -1
    return timezone(timedelta(hours=sign * int(hour_str), minutes=sign * int(minute_str)))

# Test cases for the cached_tz function
def test_cached_tz_positive():
    assert cached_tz("1", "30", "+") == timezone(timedelta(hours=1, minutes=30))

def test_cached_tz_negative():
    assert cached_tz("2", "45", "-") == timezone(timedelta(hours=-2, minutes=-45))

def test_cached_tz_zero():
    assert cached_tz("0", "0", "+") == timezone(timedelta(hours=0, minutes=0))

# Run the tests
if __name__ == "__main__":
    pytest.main()
