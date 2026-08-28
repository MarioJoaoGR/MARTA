
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.other.facter import FacterFactCollector


def test_get_facter_output_invalid():
    facter_collector = FacterFactCollector()
    module = MagicMock()
    module.return_value = "some_path"
    
    with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.find_facter', return_value=None):
        output = facter_collector.get_facter_output(module)
        assert output is None, "Expected no output when find_facter returns None"

