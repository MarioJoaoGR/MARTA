
import os
import pytest
from ansible.module_utils.common.process import get_bin_path

@pytest.fixture
def setup():
    return get_bin_path

def test_valid_case(setup):
    bin_path = setup('ls')
    assert isinstance(bin_path, str)
    assert os.path.exists(bin_path)

def test_edge_case(setup):
    with pytest.raises(ValueError):
        setup(None)
    with pytest.raises(ValueError):
        setup('')
    with pytest.raises(ValueError):
        setup('nonexistentexecutable')

def test_error_case(setup):
    with pytest.raises(ValueError):
        setup('non-existent-executable')
