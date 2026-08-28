
import pytest
from ansible.playbook.taggable import Taggable
from ansible.errors import AnsibleError

# Scenario 1: Test valid input
def test_valid_input():
    taggable = Taggable(['tag1', 'tag2'])
    assert taggable._load_tags('tags', ['tag1', 'tag2']) == ['tag1', 'tag2']

# Scenario 2: Test edge cases
def test_edge_case():
    taggable = Taggable(None)
    with pytest.raises(AnsibleError):
        taggable._load_tags('tags', None)
    
    taggable = Taggable([])
    assert taggable._load_tags('tags', []) == []

# Scenario 3: Test invalid input
def test_invalid_input():
    taggable = Taggable(['tag1', 'tag2'])
    with pytest.raises(AnsibleError):
        taggable._load_tags('tags', 123)
