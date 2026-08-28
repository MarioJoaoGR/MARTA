
import pytest
from ansible.module_utils.facts.system.chroot import ChrootFactCollector, is_chroot



def test_collect_without_module():
    collector = ChrootFactCollector()
    facts = {}
    collected_facts = collector.collect(collected_facts=facts)
    assert 'is_chroot' in collected_facts
    assert collected_facts['is_chroot'] == False