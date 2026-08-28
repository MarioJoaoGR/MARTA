
import pytest
from ansible.plugins.filter.encryption import FilterModule

@pytest.fixture(scope="module")
def filter_module():
    return FilterModule()


def test_invalid_vault_input(filter_module):
    with pytest.raises(TypeError):
        filter_module.filters()['vault']()