
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.collector import BaseFactCollector



def test_invalid_inputs():
    with pytest.raises(TypeError):
        with patch('ansible.module_utils.facts.collector.BaseFactCollector.__init__', lambda self, collectors, namespace: None):
            collector = BaseFactCollector()