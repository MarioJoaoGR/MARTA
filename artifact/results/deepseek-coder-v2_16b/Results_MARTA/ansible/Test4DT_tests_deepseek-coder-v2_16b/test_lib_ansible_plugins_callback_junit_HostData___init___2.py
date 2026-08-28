
import pytest
from ansible.plugins.callback.junit import HostData
import time

# Test initialization of HostData with valid parameters
def test_hostdata_init():
    host = HostData(uuid='1234-5678-90AB', name='HostA', status='running', result={'cpu_usage': 75, 'memory_usage': 80})
    assert host.name == 'HostA'
    assert host.status == 'running'
    assert host.result == {'cpu_usage': 75, 'memory_usage': 80}
    assert isinstance(host.finish, float)

# Test initialization of HostData with invalid parameters (missing uuid)
def test_hostdata_init_invalid():
    with pytest.raises(TypeError):
        host = HostData(name='HostA', status='running', result={'cpu_usage': 75, 'memory_usage': 80})
