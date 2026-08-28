
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import DistributionFactCollector

@pytest.fixture(autouse=True)
def mock_ansible_module():
    with patch('ansible.module_utils.basic.AnsibleModule') as MockModule:
        yield MockModule

@pytest.mark.parametrize("mock_facts", [{}])
def test_collect_with_valid_module(mock_ansible_module, mock_facts):
    # Arrange
    module = mock_ansible_module.return_value
    collector = DistributionFactCollector()
    
    # Act
    result = collector.collect(module=module)
    
    # Assert
    assert isinstance(result, dict), "Expected a dictionary but got something else."
    assert len(result) > 0, "Expected non-empty dictionary but got an empty one."

@pytest.mark.parametrize("mock_facts", [None])
def test_collect_without_module(mock_ansible_module, mock_facts):
    # Arrange
    module = mock_ansible_module.return_value
    collector = DistributionFactCollector()
    
    # Act
    result = collector.collect(module=None)
    
    # Assert
    assert isinstance(result, dict), "Expected a dictionary but got something else."
    assert len(result) == 0, "Expected empty dictionary but got something non-empty."
