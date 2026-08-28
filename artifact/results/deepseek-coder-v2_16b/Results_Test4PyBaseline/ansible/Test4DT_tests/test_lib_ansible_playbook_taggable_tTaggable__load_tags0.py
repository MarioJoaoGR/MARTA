# Module: ansible.playbook.taggable
# test_taggable.py
from ansible.playbook.taggable import Taggable
import pytest
from ansible.errors import AnsibleError

@pytest.fixture
def taggable():
    return Taggable()

def test_load_tags_from_comma_separated_string(taggable):
    tags = taggable._load_tags('tags', 'tag1, tag2, tag3')
    assert tags == ['tag1', 'tag2', 'tag3']

def test_load_tags_from_list(taggable):
    tags = taggable._load_tags('tags', ['tag1', 'tag2', 'tag3'])
    assert tags == ['tag1', 'tag2', 'tag3']

def test_load_tags_invalid_type():
    with pytest.raises(AnsibleError):
        Taggable()._load_tags('tags', 123)

def test_load_tags_empty_string():
    tags = Taggable()._load_tags('tags', '')
    assert tags == []

def test_load_tags_none_value():
    with pytest.raises(AnsibleError):
        Taggable()._load_tags('tags', None)
