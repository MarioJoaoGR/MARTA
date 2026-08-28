
import pytest
from unittest.mock import patch
from ansible.utils.color import stringc  # Assuming this module exists and has the required function

def colorize(lead, num, color):
    """ Print 'lead' = 'num' in 'color' """
    s = u"%s=%-4s" % (lead, str(num))
    if num != 0 and ANSIBLE_COLOR and color is not None:
        s = stringc(s, color)
    return s


def test_invalid_input():
    with pytest.raises(NameError):
        colorize("InvalidInput", None, "invalid_color")