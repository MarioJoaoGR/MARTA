
import pytest
from ansible.module_utils.common.text.formatters import human_to_bytes

def test_human_to_bytes_valid_conversion():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes(10, 'M') == 10485760


def test_human_to_bytes_bits_conversion():
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1Mb', default_unit='b', isbits=True) == 1048576
    assert human_to_bytes(1, 'M', isbits=True) == 1048576

def test_human_to_bytes_no_unit():
    assert human_to_bytes('10') == 10
    assert human_to_bytes(10) == 10

def test_human_to_bytes_invalid_string():
    with pytest.raises(ValueError):
        human_to_bytes('invalid')