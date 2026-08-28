
import pytest
from ansible.module_utils.facts.other.ohai import OhaiFactCollector

def test_find_ohai_valid():
    class ModuleMock:
        def get_bin_path(self, bin_name):
            if bin_name == 'ohai':
                return '/usr/local/bin/ohai'
            return None
    
    ohai_collector = OhaiFactCollector()
    module = ModuleMock()
    assert ohai_collector.find_ohai(module) == '/usr/local/bin/ohai'
