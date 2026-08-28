
import pytest
from ansible.module_utils.common.network import is_netmask

# Define a list of valid netmask values for testing
VALID_MASKS = [0, 128, 192, 224, 240, 248, 252, 254, 255]



def test_is_netmask_invalid_masks():
    invalid_masks = [3, 65, 129, 241, 253, 256]
    for mask in invalid_masks:
        assert is_netmask(mask) == False