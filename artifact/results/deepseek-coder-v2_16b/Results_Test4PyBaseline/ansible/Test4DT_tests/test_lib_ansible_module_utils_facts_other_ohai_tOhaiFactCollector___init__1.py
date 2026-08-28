
import pytest
from ansible.module_utils.facts.other.ohai import OhaiFactCollector
from ansible.module_utils.facts.namespace import PrefixFactNamespace

# Test initialization with default parameters
def test_default_initialization():
    ohai_collector = OhaiFactCollector()
    assert isinstance(ohai_collector.namespace, PrefixFactNamespace)
    assert ohai_collector.namespace.namespace_name == 'ohai'
    assert ohai_collector.namespace.prefix == 'ohai_'

# Test initialization with custom namespace and collectors
def test_custom_initialization():
    ohai_collector = OhaiFactCollector(collectors={'cpu', 'memory'}, namespace='custom_ohai')
    assert isinstance(ohai_collector.namespace, PrefixFactNamespace)