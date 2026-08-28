
import pytest
from datetime import datetime

def rfc2822_date_string(timetuple, zone='-0000'):
    """Accepts a timetuple and optional zone which defaults to ``-0000``
    and returns a date string as specified by RFC 2822, e.g.:

    Fri, 09 Nov 2001 01:08:47 -0000

    Copied from email.utils.formatdate and modified for separate use
    """
    return '%s, %02d %s %04d %02d:%02d:%02d %s' % (
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][timetuple[6]],
        timetuple[2],
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][timetuple[1] - 1],
        timetuple[0], timetuple[3], timetuple[4], timetuple[5],
        zone)

# Test scenarios

def test_valid_input_default_zone():
    timetuple = (2001, 11, 9, 1, 8, 7, 4)
    expected_output = 'Fri, 09 Nov 2001 01:08:47 -0000'
    assert rfc2822_date_string(timetuple) == expected_output

def test_valid_input_custom_zone():
    timetuple = (2001, 11, 9, 1, 8, 7, 4)
    zone = '+0530'
    expected_output = 'Fri, 09 Nov 2001 01:08:47 +0530'
    assert rfc2822_date_string(timetuple, zone) == expected_output

def test_invalid_input_none():
    timetuple = None
    with pytest.raises(TypeError):
        rfc2822_date_string(timetuple)
