
import pytest
from ansible.modules.iptables import main
from ansible.module_utils._text import to_bytes
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def setup_ansible_module():
    with patch('ansible.modules.iptables.AnsibleModule') as mock_ansible_module:
        yield mock_ansible_module

def test_valid_case(setup_ansible_module):
    # Arrange
    module = setup_ansible_module.return_value
    module.params = {
        'table': 'filter',
        'state': 'present',
        'action': 'append',
        'ip_version': 'ipv4',
        'chain': 'INPUT',
        'rule_num': None,
        'protocol': '-p tcp',
        'wait': '',
        'source': '192.168.1.0/24',
        'to_source': None,
        'destination': '172.16.0.0/16',
        'to_destination': None,
        'match': [],
        'tcp_flags': {'flags': ['SYN'], 'flags_set': []},
        'jump': 'ACCEPT',
        'gateway': None,
        'log_prefix': '',
        'log_level': None,
        'goto': None,
        'in_interface': 'eth0',
        'out_interface': 'eth1',
        'fragment': None,
        'set_counters': None,
        'source_port': '80',
        'destination_port': '8080',
        'destination_ports': [],
        'to_ports': None,
        'set_dscp_mark': None,
        'set_dscp_mark_class': None,
        'comment': 'Test comment',
        'ctstate': [],
        'src_range': None,
        'dst_range': None,
        'match_set': None,
        'match_set_flags': None,
        'limit': None,
        'limit_burst': None,
        'uid_owner': None,
        'gid_owner': None,
        'reject_with': None,
        'icmp_type': None,
        'syn': 'ignore',
        'flush': False,
        'policy': None,
    }
    module.params = to_bytes(module.params)  # Convert params to bytes for mock

    # Act
    main()

    # Assert
    module.fail_json.assert_not_called()
    module.exit_json.assert_called_with(**{
        'changed': True,
        'failed': False,
        'ip_version': 'ipv4',
        'table': 'filter',
        'chain': 'INPUT',
        'flush': False,
        'rule': '',
        'state': 'present'
    })

def test_edge_case(setup_ansible_module):
    # Arrange
    module = setup_ansible_module.return_value
    module.params = {
        'table': 'filter',
        'state': 'absent',
        'action': 'append',  # Edge case: action should be overridden by state
        'ip_version': 'ipv4',
        'chain': '',  # Empty chain name
        'rule_num': None,
        'protocol': None,
        'wait': None,
        'source': '',  # Empty source
        'to_source': None,
        'destination': '',  # Empty destination
        'to_destination': None,
        'match': [None],  # Invalid match condition
        'tcp_flags': {'flags': [], 'flags_set': []},
        'jump': 'ACCEPT',
        'gateway': None,
        'log_prefix': '',
        'log_level': None,
        'goto': None,
        'in_interface': None,
        'out_interface': None,
        'fragment': None,
        'set_counters': None,
        'source_port': None,
        'destination_port': None,
        'destination_ports': [],
        'to_ports': None,
        'set_dscp_mark': None,
        'set_dscp_mark_class': None,
        'comment': '',  # Empty comment
        'ctstate': [],
        'src_range': None,
        'dst_range': None,
        'match_set': None,
        'match_set_flags': None,
        'limit': None,
        'limit_burst': None,
        'uid_owner': None,
        'gid_owner': None,
        'reject_with': None,
        'icmp_type': None,
        'syn': 'ignore',
        'flush': False,
        'policy': None,
    }
    module.params = to_bytes(module.params)  # Convert params to bytes for mock

    # Act
    main()

    # Assert
    module.fail_json.assert_called()
    assert module.exit_json.call_count == 1
    call_args = module.exit_json.call_args[0][0]
    assert not call_args['changed']
    assert call_args['failed']

def test_invalid_inputs(setup_ansible_module):
    # Arrange
    module = setup_ansible_module.return_value
    module.params = {
        'table': 'filter',
        'state': 'present',
        'action': 'insert',  # Invalid action for this test
        'ip_version': 'ipv4',
        'chain': 'INPUT',
        'rule_num': '1',  # Rule number set but not used in insert mode
        'protocol': '-p tcp',
        'wait': '',
        'source': '192.168.1.0/24',
        'to_source': None,
        'destination': '172.16.0.0/16',
        'to_destination': None,
        'match': [],
        'tcp_flags': {'flags': ['SYN'], 'flags_set': []},
        'jump': 'ACCEPT',
        'gateway': None,
        'log_prefix': '',
        'log_level': None,
        'goto': None,
        'in_interface': 'eth0',
        'out_interface': 'eth1',
        'fragment': None,
        'set_counters': None,
        'source_port': '80',
        'destination_port': '8080',
        'destination_ports': [],
        'to_ports': None,
        'set_dscp_mark': None,
        'set_dscp_mark_class': None,
        'comment': 'Test comment',
        'ctstate': [],
        'src_range': None,
        'dst_range': None,
        'match_set': None,
        'match_set_flags': None,
        'limit': None,
        'limit_burst': None,
        'uid_owner': None,
        'gid_owner': None,
        'reject_with': None,
        'icmp_type': None,
        'syn': 'ignore',
        'flush': False,
        'policy': 'ACCEPT',  # Conflicting policy with flush
    }
    module.params = to_bytes(module.params)  # Convert params to bytes for mock

    # Act & Assert
    with pytest.raises(SystemExit):
        main()
    module.fail_json.assert_called_with(msg="Either chain or flush parameter must be specified.")
