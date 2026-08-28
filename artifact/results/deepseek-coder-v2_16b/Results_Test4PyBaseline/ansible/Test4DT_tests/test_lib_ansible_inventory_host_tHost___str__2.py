
import pytest
from ansible.inventory.host import Host

# Test string representation with only name
def test_str_representation_with_only_name():
    host = Host(name='example-host')
    assert str(host) == 'example-host'

# Test string representation with name and port
def test_str_representation_with_name_and_port():
    host = Host(name='example-host', port=22)
    assert str(host) == 'example-host'

# Test string representation without generating a UUID
def test_str_representation_without_gen_uuid():
    host = Host(name='example-host', gen_uuid=False)
    assert str(host) == 'example-host'

# Test string representation with additional variables
def test_str_representation_with_additional_vars():
    host = Host(name='example-host')
    host.set_variable('ansible_port', 22)