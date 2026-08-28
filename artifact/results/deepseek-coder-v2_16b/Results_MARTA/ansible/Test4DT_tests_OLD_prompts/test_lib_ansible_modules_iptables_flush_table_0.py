
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.iptables import push_arguments

def flush_table(iptables_path, module, params):
    cmd = push_arguments(iptables_path, '-F', params, make_rule=False)
    module.run_command(cmd, check_rc=True)

# Test for invalid inputs
def test_invalid_inputs():
    with patch('ansible.modules.iptables.push_arguments', return_value='-F filter'):
        module = MagicMock()
        params = {'other': 'key'}
        with pytest.raises(KeyError):
            flush_table('/usr/sbin/iptables', module, params)
