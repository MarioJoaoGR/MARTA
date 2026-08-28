
import pytest
from ansible.inventory.host import Host
from unittest.mock import patch
import uuid

# Test initialization with default values
def test_init_default():
    host = Host(name='example_host')
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert 'ansible_port' not in host.vars