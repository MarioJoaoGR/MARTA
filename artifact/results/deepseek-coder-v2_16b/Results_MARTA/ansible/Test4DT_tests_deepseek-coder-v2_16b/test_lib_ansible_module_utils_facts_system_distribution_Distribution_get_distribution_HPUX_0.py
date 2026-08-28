
import pytest
from ansible.module_utils.facts.system.distribution import Distribution
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="function")
def distribution():
    module = MagicMock()
    return Distribution(module)


def test_get_distribution_HPUX_no_match(distribution):
    # Mock the output of the command, no match found
    module_mock = distribution.module
    module_mock.run_command.return_value = (0, 'No matching entries', '')
    
    # Call the method under test
    result = distribution.get_distribution_HPUX()
    
    # Assertions
    assert not result