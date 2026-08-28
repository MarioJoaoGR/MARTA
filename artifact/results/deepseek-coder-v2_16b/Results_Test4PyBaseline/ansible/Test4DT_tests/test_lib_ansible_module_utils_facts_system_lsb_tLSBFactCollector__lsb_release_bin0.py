# Module: ansible.module_utils.facts.system.lsb
import ansible.module_utils.facts as facts
import pytest
from unittest.mock import MagicMock

# Assuming lsb_fact_collector is an instance of LSBFactCollector
@pytest.fixture(autouse=True)
def setup():
    lsb_fact_collector = LSBFactCollector()
    yield

def test_lsb_release_bin_with_valid_path():
    # Mock the module object with a run_command method that returns a successful result
    module = MagicMock()
    module.run_command.return_value = (0, "LSB Version:	1.4\nDistributor ID:	Ubuntu\nDescription:	Ubuntu 20.04.1 LTS\nRelease:	20.04\nCodename:	focal", "")
    
    # Call the method with a valid path and module instance
    lsb_path = '/usr/bin/lsb_release'
    facts = lsb_fact_collector._lsb_release_bin(lsb_path, module)
    
    # Assert that the returned dictionary contains the expected keys and values
    assert 'release' in facts
    assert facts['release'] == '1.4'
    assert 'id' in facts
    assert facts['id'] == 'Ubuntu'
    assert 'description' in facts
    assert facts['description'] == 'Ubuntu 20.04.1 LTS'
    assert 'codename' in facts
    assert facts['codename'] == 'focal'

def test_lsb_release_bin_with_invalid_path():
    # Mock the module object with a run_command method that returns an error result
    module = MagicMock()
    module.run_command.return_value = (1, "", "Error: Cannot find lsb_release binary")
    
    # Call the method with an invalid path and module instance
    lsb_path = None
    facts = lsb_fact_collector._lsb_release_bin(lsb_path, module)
    
    # Assert that the returned dictionary is empty
    assert not facts

def test_lsb_release_bin_with_empty_output():
    # Mock the module object with a run_command method that returns an empty output result
    module = MagicMock()
    module.run_command.return_value = (0, "", "")
    
    # Call the method with a valid path and module instance
    lsb_path = '/usr/bin/lsb_release'
    facts = lsb_fact_collector._lsb_release_bin(lsb_path, module)
    
    # Assert that the returned dictionary is empty
    assert not facts
