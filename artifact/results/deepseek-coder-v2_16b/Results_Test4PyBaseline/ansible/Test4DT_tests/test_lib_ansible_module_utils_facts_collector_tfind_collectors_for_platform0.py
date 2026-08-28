
import pytest
from ansible.module_utils.facts.collector import find_collectors_for_platform

# Define test classes for collectors
class Collector1:
    def __init__(self):
        self.platforms = ['Linux', 'Windows']
    
    def platform_match(self, compat_platform):
        return compat_platform in self.platforms

class Collector2:
    def __init__(self):
        self.platforms = ['Linux']
    
    def platform_match(self, compat_platform):
        return compat_platform == 'Linux'

class Collector3:
    def __init__(self):
        self.platforms = ['Windows']
    
    def platform_match(self, compat_platform):
        return compat_platform == 'Linux'

class Collector4:
    def __init__(self):
        self.platforms = ['Linux', 'SunOS']
    
    def platform_match(self, compat_platform):
        return compat_platform in self.platforms

class Collector5:
    def __init__(self):
        self.platforms = ['SunOS']
    
    def platform_match(self, compat_platform):
        return compat_platform == 'SunOS'

# Define test cases for find_collectors_for_platform function
@pytest.mark.parametrize("all_collector_classes, compat_platforms, expected", [
    (
        [Collector1(), Collector2()],  # all_collector_classes
        ['Linux', 'Windows'],           # compat_platforms
        {Collector1()}                   # expected
    ),
    (
        [Collector3()],                  # all_collector_classes
        ['MacOS'],                       # compat_platforms
        set()                            # expected
    ),
    (
        [Collector4(), Collector5()],    # all_collector_classes
        ['SunOS', 'Linux'],              # compat_platforms
        {Collector4(), Collector5()}     # expected
    )
])
def test_find_collectors_for_platform(all_collector_classes, compat_platforms, expected):
    compatible_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert set(compatible_collectors) == expected
