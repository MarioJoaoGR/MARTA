
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.chroot import ChrootFactCollector

def test_valid_input():
    collector = ChrootFactCollector()
    module = MagicMock()
    collected_facts = {}
    
    with pytest.raises(Exception):
        collector.collect(module=module, collected_facts=collected_facts)
