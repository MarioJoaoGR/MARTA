
import pytest
from ansible.module_utils.facts.collector import CollectorA, CollectorB  # Assuming these are defined elsewhere
from collections import defaultdict

def build_fact_id_to_collector_map(collectors_for_platform):
    fact_id_to_collector_map = defaultdict(list)
    aliases_map = defaultdict(set)

    for collector_class in collectors_for_platform:
        primary_name = collector_class.name

        fact_id_to_collector_map[primary_name].append(collector_class)

        for fact_id in collector_class._fact_ids:
            fact_id_to_collector_map[fact_id].append(collector_class)
            aliases_map[primary_name].add(fact_id)

    return fact_id_to_collector_map, aliases_map

# Test Case 1: Basic Functionality with Two Collectors
def test_build_fact_id_to_collector_map_basic():
    class CollectorA:
        name = 'CollectorA'
        fact_ids = ['fact1', 'fact2']

    class CollectorB:
        name = 'CollectorB'
        fact_ids = ['fact2', 'fact3']

    collectors = [CollectorA(), CollectorB()]
    result = build_fact_id_to_collector_map(collectors)
    
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "There should be two dictionaries in the result"
    
    fact_id_to_collector_map, aliases_map = result
    
    assert 'CollectorA' in fact_id_to_collector_map, "fact_id_to_collector_map should contain CollectorA"
    assert len(fact_id_to_collector_map['CollectorA']) == 1, "CollectorA should have one entry"
    
    assert 'fact1' in fact_id_to_collector_map, "fact_id_to_collector_map should contain fact1"
    assert len(fact_id_to_collector_map['fact1']) == 1, "fact1 should have one entry"
    
    assert 'CollectorB' in aliases_map, "aliases_map should contain CollectorB"
    assert 'fact2' in aliases_map['CollectorB'], "aliases_map for CollectorB should include fact2"
    assert 'fact3' in aliases_map['CollectorB'], "aliases_map for CollectorB should include fact3"

# Test Case 2: Functionality with a Single Custom Collector
def test_build_fact_id_to_collector_map_custom():
    class CustomCollector:
        name = 'CustomCollector'
        fact_ids = ['custom1', 'custom2']

    collectors = [CustomCollector()]
    result = build_fact_id_to_collector_map(collectors)
    
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "There should be two dictionaries in the result"
    
    fact_id_to_collector_map, aliases_map = result
    
    assert 'CustomCollector' in fact_id_to_collector_map, "fact_id_to_collector_map should contain CustomCollector"
    assert len(fact_id_to_collector_map['CustomCollector']) == 1, "CustomCollector should have one entry"
    
    assert 'custom1' in fact_id_to_collector_map, "fact_id_to_collector_map should contain custom1"
    assert len(fact_id_to_collector_map['custom1']) == 1, "custom1 should have one entry"
    
    assert 'CustomCollector' in aliases_map, "aliases_map should contain CustomCollector"
    assert 'custom1' in aliases_map['CustomCollector'], "aliases_map for CustomCollector should include custom1"
    assert 'custom2' in aliases_map['CustomCollector'], "aliases_map for CustomCollector should include custom2"

# Test Case 3: Functionality with Multiple Collectors
def test_build_fact_id_to_collector_map_multiple():
    class AnotherCollector:
        name = 'AnotherCollector'
        fact_ids = ['another1', 'another2']

    collectors = [AnotherCollector()]
    result = build_fact_id_to_collector_map(collectors)
    
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "There should be two dictionaries in the result"
    
    fact_id_to_collector_map, aliases_map = result
    
    assert 'AnotherCollector' in fact_id_to_collector_map, "fact_id_to_collector_map should contain AnotherCollector"
    assert len(fact_id_to_collector_map['AnotherCollector']) == 1, "AnotherCollector should have one entry"
    
    assert 'another1' in fact_id_to_collector_map, "fact_id_to_collector_map should contain another1"
    assert len(fact_id_to_collector_map['another1']) == 1, "another1 should have one entry"
    
    assert 'AnotherCollector' in aliases_map, "aliases_map should contain AnotherCollector"
    assert 'another1' in aliases_map['AnotherCollector'], "aliases_map for AnotherCollector should include another1"
    assert 'another2' in aliases_map['AnotherCollector'], "aliases_map for AnotherCollector should include another2"

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
_ ERROR collecting test_lib_ansible_module_utils_facts_collector_build_fact_id_to_collector_map_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_build_fact_id_to_collector_map_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_build_fact_id_to_collector_map_0.py:3: in <module>
    from ansible.module_utils.facts.collector import CollectorA, CollectorB  # Assuming these are defined elsewhere
E   ImportError: cannot import name 'CollectorA' from 'ansible.module_utils.facts.collector' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/facts/collector.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_build_fact_id_to_collector_map_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.42s ===============================
"""