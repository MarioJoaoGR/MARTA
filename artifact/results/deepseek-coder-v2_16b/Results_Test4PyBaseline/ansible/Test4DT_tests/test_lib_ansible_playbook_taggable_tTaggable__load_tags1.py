
# Module: ansible.playbook.taggable
# test_taggable.py
from ansible.playbook.taggable import Taggable
import pytest
from ansible.errors import AnsibleError

@pytest.fixture
def taggable():
    return Taggable()

# Test case for when ds is a list (already covered by existing test_load_tags_from_list)

# Test case for when ds is a string, but not comma-separated (should be treated as a single element list)
def test_load_tags_single_string(taggable):
    tags = taggable._load_tags('tags', 'tag1')
    assert tags == ['tag1']

# Test case for when ds is None (should raise AnsibleError)
def test_load_tags_none_value(taggable):
    with pytest.raises(AnsibleError):
        Taggable()._load_tags('tags', None)

# Test case for handling empty string (should be treated as an empty list)
def test_load_tags_empty_string(taggable):
    tags = taggable._load_tags('tags', '')