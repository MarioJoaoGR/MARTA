
import pytest
from ansible.module_utils.facts.other.ohai import OhaiFactCollector



def test_invalid_input():
    ohai_collector = OhaiFactCollector()
    module_mock = {'fact_path': 'invalid_module'}
    assert hasattr(ohai_collector, 'get_ohai_output')
    with pytest.raises(AttributeError):
        output = ohai_collector.get_ohai_output(module_mock)