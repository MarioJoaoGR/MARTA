
import pytest
import time
from ansible.module_utils.urls import rfc2822_date_string

# Test cases for the rfc2822_date_string function
def test_rfc2822_date_string_default_zone():
    # Get the current local time as a tuple
    timetuple = time.localtime()
    
    # Call the function with the local time tuple and default zone
    date_string = rfc2822_date_string(timetuple)
    
    # Check if the output format matches the expected RFC 2822 format
    assert isinstance(date_string, str), "Expected a string"
    assert len(date_string.split()) == 6, "Expected six parts in the date string"
    assert date_string.startswith(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][timetuple[6].tm_wday]), "Incorrect weekday format"
    assert int(date_string.split()[1][1:]) == timetuple[2], "Incorrect day of month"
    assert date_string.split()[1][0] in ['J', 'F', 'M', 'A', 'Y', 'U', 'O'], "Incorrect month format"
    assert int(date_string.split()[3]) == timetuple[0], "Incorrect year"
    assert int(date_string.split()[4].split(':')[0]) == timetuple[3], "Incorrect hour"
    assert int(date_string.split()[4].split(':')[1]) == timetuple[4], "Incorrect minute"
    assert int(date_string.split()[4].split(':')[2]) == timetuple[5], "Incorrect second"
    assert date_string.endswith('-0000'), "Expected default zone '-0000'"

def test_rfc2822_date_string_custom_zone():
    # Get the current local time as a tuple
    timetuple = time.localtime()
    
    # Call the function with the local time tuple and a custom zone
    date_string = rfc2822_date_string(timetuple, zone='+0100')
    
    # Check if the output format matches the expected RFC 2822 format with custom zone
    assert isinstance(date_string, str), "Expected a string"
    assert len(date_string.split()) == 6, "Expected six parts in the date string"
    assert date_string.startswith(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][timetuple[6].tm_wday]), "Incorrect weekday format"
    assert int(date_string.split()[1][1:]) == timetuple[2], "Incorrect day of month"
    assert date_string.split()[1][0] in ['J', 'F', 'M', 'A', 'Y', 'U', 'O'], "Incorrect month format"
    assert int(date_string.split()[3]) == timetuple[0], "Incorrect year"
    assert int(date_string.split()[4].split(':')[0]) == timetuple[3], "Incorrect hour"
    assert int(date_string.split()[4].split(':')[1]) == timetuple[4], "Incorrect minute"
    assert int(date_string.split()[4].split(':')[2]) == timetuple[5], "Incorrect second"
    assert date_string.endswith('+0100'), "Expected custom zone '+0100'"

def test_rfc2822_date_string_direct_call():
    # Get the current local time as a tuple and call the function directly
    timetuple = time.localtime()
    date_string = rfc2822_date_string(timetuple)
    
    # Check if the output format matches the expected RFC 2822 format with default zone
    assert isinstance(date_string, str), "Expected a string"
    assert len(date_string.split()) == 6, "Expected six parts in the date string"
    assert date_string.startswith(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][timetuple[6].tm_wday]), "Incorrect weekday format"
    assert int(date_string.split()[1][1:]) == timetuple[2], "Incorrect day of month"
    assert date_string.split()[1][0] in ['J', 'F', 'M', 'A', 'Y', 'U', 'O'], "Incorrect month format"
    assert int(date_string.split()[3]) == timetuple[0], "Incorrect year"
    assert int(date_string.split()[4].split(':')[0]) == timetuple[3], "Incorrect hour"
    assert int(date_string.split()[4].split(':')[1]) == timetuple[4], "Incorrect minute"
    assert int(date_string.split()[4].split(':')[2]) == timetuple[5], "Incorrect second"
    assert date_string.endswith('-0000'), "Expected default zone '-0000'"
