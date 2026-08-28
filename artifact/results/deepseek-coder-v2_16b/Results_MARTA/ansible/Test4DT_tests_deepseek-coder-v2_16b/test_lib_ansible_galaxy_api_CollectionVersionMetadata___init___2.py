
import pytest
from ansible.galaxy.api import CollectionVersionMetadata

def test_invalid_inputs():
    # Test that initializing with invalid inputs raises a ValueError
    with pytest.raises(TypeError):
        CollectionVersionMetadata()
