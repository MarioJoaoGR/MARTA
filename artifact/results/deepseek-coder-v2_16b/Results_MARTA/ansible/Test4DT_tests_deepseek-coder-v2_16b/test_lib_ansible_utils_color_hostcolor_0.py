
import pytest
from ansible.utils.color import C

# Assuming the hostcolor function is defined as per the provided documentation
def hostcolor(host, stats, color=True):
    if ANSIBLE_COLOR and color:
        if stats['failures'] != 0 or stats['unreachable'] != 0:
            return u"%-37s" % stringc(host, C.COLOR_ERROR)
        elif stats['changed'] != 0:
            return u"%-37s" % stringc(host, C.COLOR_CHANGED)
        else:
            return u"%-37s" % stringc(host, C.COLOR_OK)
    return u"%-26s" % host

# Test cases for the hostcolor function
def test_valid_case_default_color():
    host = 'localhost'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    result = hostcolor(host, stats)
    assert result == 'localhost'

def test_valid_case_no_color():
    host = 'localhost'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    result = hostcolor(host, stats, color=False)
    assert result == 'localhost'

def test_invalid_case_all_zero():
    host = 'localhost'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    result = hostcolor(host, stats)
    assert result == '\033[38;5;2mlocalhost\033[0m'
