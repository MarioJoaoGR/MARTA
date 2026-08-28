
import pytest
from ansible.modules.iptables import push_arguments, construct_rule


def test_invalid_inputs():
    with pytest.raises(KeyError):
        push_arguments('/usr/sbin/iptables', '-A', {'table': 'filter', 'chain': 'INPUT'})


def test_insert_rule_with_invalid_num():
    with pytest.raises(KeyError):
        push_arguments('/usr/sbin/iptables', '-I', {'table': 'filter', 'chain': 'INPUT'})