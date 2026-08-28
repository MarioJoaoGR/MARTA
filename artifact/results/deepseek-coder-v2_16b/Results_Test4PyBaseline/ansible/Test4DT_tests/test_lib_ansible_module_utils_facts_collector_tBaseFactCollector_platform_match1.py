
# Module: ansible.module_utils.facts.collector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_basefactcollector_platform_match():
    # Test platform matching with a matching platform
    platform_info = {'system': 'Generic'}
    matched_class = BaseFactCollector.platform_match(platform_info)
    assert matched_class is BaseFactCollector

    # Test platform matching with a non-matching platform
    platform_info = {'system': 'Linux'}
    matched_class = BaseFactCollector.platform_match(platform_info)
    assert matched_class is None

def test_basefactcollector_platform_match_none():
    # Test platform matching with no platform information provided
    platform_info = {}
    matched_class = BaseFactCollector.platform_match(platform_info)
    assert matched_class is None

def test_basefactcollector_platform_match_empty():
    # Test platform matching with an empty dictionary (no platform info)
    platform_info = {'system': None}
    matched_class = BaseFactCollector.platform_match(platform_info)
    assert matched_class is None
