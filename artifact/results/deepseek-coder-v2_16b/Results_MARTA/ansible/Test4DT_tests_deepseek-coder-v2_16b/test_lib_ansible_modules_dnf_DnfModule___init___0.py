
import pytest
from ansible.modules.dnf import DnfModule

@pytest.fixture
def valid_module():
    return {'params': {'allowerasing': True, 'nobest': False}}

@pytest.fixture
def edge_case_module():
    return {'params': {'allowerasing': None, 'nobest': False}}

@pytest.fixture
def invalid_module():
    return {'params': {'allowerasing': 'invalid', 'nobest': 123}}

def test_valid_inputs(valid_module):
    dnf_module = DnfModule(module=valid_module)
    assert dnf_module.allowerasing is True
    assert dnf_module.nobest is False

def test_edge_cases(edge_case_module):
    with pytest.raises(TypeError):
        DnfModule(module=edge_case_module)

def test_invalid_inputs(invalid_module):
    with pytest.raises(TypeError):
        DnfModule(module=invalid_module)
