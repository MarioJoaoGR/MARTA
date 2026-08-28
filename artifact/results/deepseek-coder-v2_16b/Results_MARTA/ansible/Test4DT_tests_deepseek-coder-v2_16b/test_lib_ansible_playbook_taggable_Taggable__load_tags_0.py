
import pytest
from ansible.playbook.taggable import Taggable
from ansible.errors import AnsibleError


def test_invalid_input():
    with pytest.raises(AnsibleError) as excinfo:
        Taggable()._load_tags('tags', 123)
    assert str(excinfo.value) == "tags must be specified as a list"