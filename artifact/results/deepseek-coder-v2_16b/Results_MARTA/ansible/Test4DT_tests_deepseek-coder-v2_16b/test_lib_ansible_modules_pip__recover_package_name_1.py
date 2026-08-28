
import pytest
from ansible.modules.pip import _recover_package_name



def test_recover_package_name_valid_mixed():
    names = ['django>1.11.1', '<1.11.3', 'ipaddress', 'simpleproject>1.1.0', '<2.0.0']
    expected = ['django>1.11.1,<1.11.3', 'ipaddress', 'simpleproject>1.1.0,<2.0.0']
    assert _recover_package_name(names) == expected, f"Expected {expected}, but got {_recover_package_name(names)}"

def test_recover_package_name_multiple_lines():
    names = ['django>1.11.1,<1.11.3,ipaddress', 'simpleproject>1.1.0,<2.0.0']
    expected = ['django>1.11.1,<1.11.3', 'ipaddress', 'simpleproject>1.1.0,<2.0.0']
    assert _recover_package_name(names) == expected, f"Expected {expected}, but got {_recover_package_name(names)}"