
import pytest
from mimesis.providers import Internet

def test_valid_mac_address():
    internet_instance = Internet()
    mac_address = internet_instance.mac_address()
    assert isinstance(mac_address, str), "Expected a string MAC address"
    assert len(mac_address.split(':')) == 6, "Expected 6 parts in the MAC address"
    for part in mac_address.split(':'):
        assert int(part, 16) <= 0xff, f"Part {part} is out of range (0x00 to 0xff)"
