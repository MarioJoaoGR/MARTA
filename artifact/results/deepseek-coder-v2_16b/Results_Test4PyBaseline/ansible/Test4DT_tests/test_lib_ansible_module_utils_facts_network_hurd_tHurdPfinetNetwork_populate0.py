
import os
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

def test_populate_with_default_parameters():
    module = AnsibleModule(argument_spec={})
    instance = HurdPfinetNetwork(module)
    network_facts = instance.populate()
    assert isinstance(network_facts, dict), "Expected a dictionary but got something else."
    assert 'interfaces' not in network_facts, "Expected no interfaces to be present initially."

def test_populate_with_custom_socket_dir():
    HurdPfinetNetwork._socket_dir = '/custom/path/to/sockets/'
    module = AnsibleModule(argument_spec={})
    instance = HurdPfinetNetwork(module)
    network_facts = instance.populate()
    assert isinstance(network_facts, dict), "Expected a dictionary but got something else."
    assert 'interfaces' not in network_facts, "Expected no interfaces to be present initially."

def test_populate_with_collected_facts():
    collected_facts = {
        'interfaces': ['eth0', 'eth1'],
        'eth0': {'active': True, 'device': 'eth0', 'ipv4': {'address': '192.168.1.100'}, 'ipv6': [{'address': '2001:db8::1', 'prefix': '64'}]},
        'eth1': {'active': False, 'device': 'eth1', 'ipv4': {}, 'ipv6': []}
    }
    module = AnsibleModule(argument_spec={})
    instance = HurdPfinetNetwork(module)
    network_facts = instance.populate(collected_facts=collected_facts)
    assert isinstance(network_facts, dict), "Expected a dictionary but got something else."
    assert 'interfaces' in network_facts, "Expected interfaces to be present."
    assert len(network_facts['interfaces']) == 2, "Expected two interfaces to be present."
    assert network_facts['eth0']['active'] is True, "Expected eth0 to be active."
    assert network_facts['eth1']['active'] is False, "Expected eth1 to not be active."

def test_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    instance = HurdPfinetNetwork(module)
    network_facts = {}
    fsysopts_path = 'fsysopts'
    socket_path = '/servers/socket/inet'
    result = instance.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert isinstance(result, dict), "Expected a dictionary but got something else."
    assert 'interfaces' in result, "Expected interfaces to be present."
    assert len(result['interfaces']) == 1, "Expected one interface to be parsed from fsysopts output."
