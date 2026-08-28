
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.taggable import Taggable
from typing import Set, Dict, Any

class MockTaggable(Taggable):
    def __init__(self):
        self.tags = ['tag1', 'tag2']  # Example tags for testing
        self._loader = MagicMock()



def test_missing_tags_handling():
    obj = MockTaggable()
    with patch('ansible.playbook.taggable.Templar', MagicMock):
        only_tags: Set[str] = set()
        skip_tags: Set[str] = set()
        all_vars: Dict[str, Any] = {'tags': ['tag1', 'tag2']}
        result = obj.evaluate_tags(only_tags, skip_tags, all_vars)
        assert result is True