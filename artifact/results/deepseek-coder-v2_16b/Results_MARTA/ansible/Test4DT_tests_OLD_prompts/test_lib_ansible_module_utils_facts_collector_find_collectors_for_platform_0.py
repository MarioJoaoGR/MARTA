
import pytest
from unittest.mock import patch
from ansible.module_utils.facts.collector import find_collectors_for_platform

# Define some collector classes for testing
class CollectorClass1:
    def __init__(self):
        self.name = "Collector 1"
    
    def platform_match(self, platform):
        return platform == "PlatformA" or platform == "PlatformB"

class CollectorClass2:
    def __init__(self):
        self.name = "Collector 2"
    
    def platform_match(self, platform):
        return platform == "PlatformC"

class CollectorClass3:
    def __init__(self):
        self.name = "Collector 3"
    
    def platform_match(self, platform):
        return False

class CollectorClass4:
    def __init__(self):
        self.name = "Collector 4"
    
    def platform_match(self, platform):
        return True

# Define the test functions

def test_no_compatible():
    all_collectors = {CollectorClass3()}
    platforms = ["PlatformA", "PlatformB"]
    
    with patch('ansible.module_utils.facts.collector.find_collectors_for_platform', return_value={}):
        compatible_collectors = find_collectors_for_platform(all_collectors, platforms)
        assert set([collector.__class__.__name__ for collector in compatible_collectors]) == set()
