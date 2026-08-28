
import pytest
from unittest.mock import patch
import subprocess
import re

# Assuming get_chain_policy is defined in a module named iptables_module
def get_chain_policy(iptables_path, module, params):
    cmd = push_arguments(iptables_path, '-L', params, make_rule=False)
    rc, out, _ = module.run_command(cmd, check_rc=True)
    chain_header = out.split("\n")[0]
    result = re.search(r'\(policy ([A-Z]+)\)', chain_header)
    if result:
        return result.group(1)
    return None

# Mock module for testing
class ModuleMock:
    def run_command(self, cmd, check_rc=True):
        if "invalid" in cmd:
            return 1, "", ""
        elif "missing" in cmd:
            return 0, "No such file or directory", ""
        else:
            return 0, "iptables output with policy ACCEPT", ""

# Test cases
@pytest.mark.parametrize("params, expected", [
    ({'table': 'filter', 'chain': 'INPUT'}, 'ACCEPT'),
    ({'table': 'nat', 'chain': 'PREROUTING'}, None),
])
def test_valid_input(params, expected):
    with patch('subprocess.run') as mock_run:
        mock_run.return_value = subprocess.CompletedProcess([''], 0, "iptables output with policy ACCEPT")
        module = ModuleMock()
        result = get_chain_policy('/usr/sbin/iptables', module, params)
        assert result == expected

def test_missing_lines():
    module = ModuleMock()
    result = get_chain_policy('/usr/sbin/iptables', module, {'table': 'filter', 'chain': 'NONEXISTENT'})
    assert result is None

@pytest.mark.parametrize("params", [
    ({'table': 'invalid', 'chain': 'INPUT'}),
    ({'table': 'filter', 'chain': 'INVALID'}),
])
def test_invalid_input(params):
    module = ModuleMock()
    result = get_chain_policy('/usr/sbin/iptables', module, params)
    assert result is None
