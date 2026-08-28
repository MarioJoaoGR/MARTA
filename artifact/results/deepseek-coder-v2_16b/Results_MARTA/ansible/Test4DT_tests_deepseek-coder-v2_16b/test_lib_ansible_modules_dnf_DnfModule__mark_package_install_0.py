
import pytest
from ansible.modules.dnf import DnfModule

@pytest.fixture
def valid_module():
    return {'params': {'allowerasing': True, 'nobest': False}}

@pytest.fixture
def edge_cases_module():
    return {'params': {'allowerasing': False, 'nobest': True}}

@pytest.fixture
def invalid_module():
    return {'params': {'allowerasing': None, 'nobest': None}}

def test_valid_inputs(valid_module):
    dnf_module = DnfModule(module=valid_module)
    assert dnf_module.allowerasing is True
    assert dnf_module.nobest is False

def test_edge_cases(edge_cases_module):
    dnf_module = DnfModule(module=edge_cases_module)
    assert dnf_module.allowerasing is False
    assert dnf_module.nobest is True

def test_invalid_inputs(invalid_module):
    with pytest.raises(TypeError):
        DnfModule(module=invalid_module)
