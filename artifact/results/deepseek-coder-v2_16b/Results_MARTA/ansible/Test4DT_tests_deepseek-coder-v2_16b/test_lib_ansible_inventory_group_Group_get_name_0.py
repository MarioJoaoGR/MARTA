
import pytest
from ansible.inventory.group import Group

def test_valid_name():
    group = Group(name="webservers")
    assert group.get_name() == "webservers"


