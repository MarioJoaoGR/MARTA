
import pytest
from lib.ansible.plugins.callback import HostData
import time

def test_valid_inputs():
    host = HostData(uuid='1234-5678-90AB', name='HostA', status='running', result={'cpu_usage': 75, 'memory_usage': 80})
    assert host.uuid == '1234-5678-90AB'
    assert host.name == 'HostA'
    assert host.status == 'running'
    assert host.result == {'cpu_usage': 75, 'memory_usage': 80}

def test_edge_cases():
    with pytest.raises(TypeError):
        HostData(uuid=None, name='', status='', result={})

def test_invalid_inputs():
    with pytest.raises(TypeError):
        HostData(uuid=12345, name='HostA', status='running', result={'cpu_usage': 75, 'memory_usage': 80})
