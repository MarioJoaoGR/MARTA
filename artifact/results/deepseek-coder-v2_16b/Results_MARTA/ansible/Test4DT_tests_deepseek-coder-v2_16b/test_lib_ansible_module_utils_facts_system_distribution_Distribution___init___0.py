
import pytest
from ansible.module_utils.facts.system.distribution import Distribution
import os

@pytest.fixture(scope="module")
def module():
    return type('MockModule', (object,), {'params': {}})()

@pytest.fixture(scope="module")
def distro(module):
    return Distribution(module)

def test_none_input(distro):
    with pytest.raises(TypeError):
        Distribution()
