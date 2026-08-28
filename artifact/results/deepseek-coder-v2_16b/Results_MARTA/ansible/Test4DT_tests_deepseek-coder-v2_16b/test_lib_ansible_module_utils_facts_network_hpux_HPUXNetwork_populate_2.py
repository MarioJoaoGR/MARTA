
import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture(scope="module")
def hpux_network():
    return HPUXNetwork()


def test_edge_case_none():
    with pytest.raises(TypeError):
        hpux_network = HPUXNetwork()  # This should raise a TypeError as per the error message