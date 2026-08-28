
import pytest
import time
from ansible.module_utils.urls import rfc2822_date_string

# Test case to check the construction of the date string with default zone
def test_rfc2822_date_string_default_zone():
    timetuple = time.localtime()
    date_string = rfc2822_date_string(timetuple)
    
    assert isinstance(date_string, str), "Expected a string"
    parts = date_string.split()
    assert len(parts) == 6, "Expected six parts in the date string"