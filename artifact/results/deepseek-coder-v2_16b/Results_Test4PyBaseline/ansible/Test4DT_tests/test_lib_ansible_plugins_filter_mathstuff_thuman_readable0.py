# Module: ansible.plugins.filter.mathstuff
import pytest
from ansible.plugins.filter import mathstuff

# Test cases for human_readable function
def test_human_readable_default():
    assert mathstuff.human_readable(1024) == '1.0K'

def test_human_readable_bits():
    assert mathstuff.human_readable(5000, isbits=True) == '4.9K'

def test_human_readable_specified_unit():
    assert mathstuff.human_readable(2048, unit='M') == '2.0M'

def test_human_readable_large_size():
    assert mathstuff.human_readable(1048576) == '1.0M'

def test_human_readable_invalid_input():
    with pytest.raises(mathstuff.AnsibleFilterError):
        mathstuff.human_readable("invalid input")

def test_human_readable_negative_size():
    with pytest.raises(mathstuff.AnsibleFilterTypeError):
        mathstuff.human_readable(-1024)
