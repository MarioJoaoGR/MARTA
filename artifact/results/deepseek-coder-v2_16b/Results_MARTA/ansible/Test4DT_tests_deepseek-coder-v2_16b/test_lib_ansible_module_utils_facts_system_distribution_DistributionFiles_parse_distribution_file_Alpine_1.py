
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture(scope="module")
def distro_files():
    return DistributionFiles(module='test_module')


def test_error_case():
    with pytest.raises(ValueError):
        raise ValueError("Test error case")