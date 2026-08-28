
import pytest
from ansible.playbook.taggable import Taggable

@pytest.fixture
def taggable_instance():
    return Taggable()

# Test scenario 1: Valid input with only_tags provided
def test_valid_input_with_only_tags(taggable_instance):
    taggable_instance._tags = ['tag1', 'tag2']
    result = taggable_instance.evaluate_tags({'tag1'}, set(), {'tags': ['tag1', 'tag2']})
    assert result is True

# Test scenario 2: No tags provided
def test_edge_case_no_tags(taggable_instance):
    taggable_instance._tags = []
    result = taggable_instance.evaluate_tags(set(), set(), {'tags': []})
    assert result is True

# Test scenario 3: Invalid input with skip_tags provided
def test_invalid_input_with_skip_tags(taggable_instance):
    taggable_instance._tags = ['tag1', 'tag2']
    result = taggable_instance.evaluate_tags(set(), {'all'}, {'tags': ['always']})
    assert result is False
