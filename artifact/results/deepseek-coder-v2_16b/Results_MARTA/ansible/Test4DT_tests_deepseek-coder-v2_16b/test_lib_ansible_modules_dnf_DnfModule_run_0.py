
import pytest
from ansible.modules.dnf import DnfModule

@pytest.fixture(scope="module")
def dnf_module():
    module_params = {
        'allowerasing': True,  # Allow packages to erase existing ones during installation
        'nobest': False         # Prevent the use of best matches in package selection
    }
    return DnfModule(module={'params': module_params})



def test_error_case():
    with pytest.raises(AttributeError):
        # Attempt to instantiate DnfModule without providing the correct parameters
        module_params = {}  # Missing 'allowerasing' and 'nobest' params
        DnfModule(module={'params': module_params})