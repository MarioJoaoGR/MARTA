
import pytest
from ansible.module_utils.facts.collector import CollectorClass1, CollectorClass2, InvalidPlatformObject

def find_collectors_for_platform(all_collector_classes, compat_platforms):
    found_collectors = set()
    found_collectors_names = set()

    for compat_platform in compat_platforms:
        platform_match = None
        for all_collector_class in all_collector_classes:
            if not hasattr(all_collector_class, 'platform_match'):
                continue
            platform_match = all_collector_class.platform_match(compat_platform)
            if platform_match:
                primary_name = getattr(all_collector_class, 'name', '')
                if primary_name not in found_collectors_names:
                    found_collectors.add(all_collector_class)
                    found_collectors_names.add(primary_name)
    return found_collectors

# Test Case 1: Basic Usage
def test_find_collectors_for_platform_basic():
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

    all_collectors = {CollectorClass1(), CollectorClass2()}
    platforms = ["PlatformB", "PlatformD"]

    compatible_collectors = find_collectors_for_platform(all_collectors, platforms)
    assert len(compatible_collectors) == 2
    collector_names = [collector.__class__.__name__ for collector in compatible_collectors]
    assert "CollectorClass1" in collector_names
    assert "CollectorClass2" in collector_names

# Test Case 2: No Compatible Collectors
def test_find_collectors_for_platform_no_compatible():
    class CollectorClass3:
        def __init__(self):
            self.name = "Collector 3"
        
        def platform_match(self, platform):
            return False

    all_collectors = {CollectorClass3()}
    platforms = ["PlatformA", "PlatformB"]

    compatible_collectors = find_collectors_for_platform(all_collectors, platforms)
    assert len(compatible_collectors) == 0

# Test Case 3: All Collectors Compatible
def test_find_collectors_for_platform_all_compatible():
    class CollectorClass4:
        def __init__(self):
            self.name = "Collector 4"
        
        def platform_match(self, platform):
            return True

    all_collectors = {CollectorClass4()}
    platforms = ["PlatformA", "PlatformB"]

    compatible_collectors = find_collectors_for_platform(all_collectors, platforms)
    assert len(compatible_collectors) == 1
    collector_names = [collector.__class__.__name__ for collector in compatible_collectors]
    assert "CollectorClass4" in collector_names

# Test Case 4: Multiple Collectors and Platforms
def test_find_collectors_for_platform_multiple():
    class CollectorClass5:
        def __init__(self):
            self.name = "Collector 5"
        
        def platform_match(self, platform):
            return platform == "PlatformX"

    class CollectorClass6:
        def __init__(self):
            self.name = "Collector 6"
        
        def platform_match(self, platform):
            return platform == "PlatformY"

    all_collectors = {CollectorClass5(), CollectorClass6()}
    platforms = ["PlatformX", "PlatformZ"]

    compatible_collectors = find_collectors_for_platform(all_collectors, platforms)
    assert len(compatible_collectors) == 2
    collector_names = [collector.__class__.__name__ for collector in compatible_collectors]
    assert "CollectorClass5" in collector_names
    assert "CollectorClass6" in collector_names

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_module_utils_facts_collector_find_collectors_for_platform_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_find_collectors_for_platform_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_find_collectors_for_platform_0.py:3: in <module>
    from ansible.module_utils.facts.collector import CollectorClass1, CollectorClass2, InvalidPlatformObject
E   ImportError: cannot import name 'CollectorClass1' from 'ansible.module_utils.facts.collector' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/facts/collector.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_find_collectors_for_platform_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.43s ===============================
"""