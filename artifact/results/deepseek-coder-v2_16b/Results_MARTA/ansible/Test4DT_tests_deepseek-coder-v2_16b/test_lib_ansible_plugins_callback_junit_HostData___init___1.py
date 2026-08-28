
import pytest
from ansible.plugins.callback.junit import HostData
import time

# Test initialization of HostData class
def test_hostdata_initialization():
    uuid = '1234-5678-90AB'
    name = 'HostA'
    status = 'running'
    result = {'cpu_usage': 75, 'memory_usage': 80}
    
    host = HostData(uuid=uuid, name=name, status=status, result=result)
    
    assert host.uuid == uuid
    assert host.name == name
    assert host.status == status
    assert host.result == result
    assert isinstance(host.finish, float)  # finish should be a timestamp in seconds since the epoch

# Test that HostData requires all parameters to initialize correctly
def test_hostdata_missing_parameters():
    with pytest.raises(TypeError):
        HostData()  # Missing required parameters

    with pytest.raises(TypeError):
        HostData(uuid='1234-5678-90AB')  # Missing name and status

    with pytest.raises(TypeError):
        HostData(name='HostA', status='running')  # Missing uuid and result
