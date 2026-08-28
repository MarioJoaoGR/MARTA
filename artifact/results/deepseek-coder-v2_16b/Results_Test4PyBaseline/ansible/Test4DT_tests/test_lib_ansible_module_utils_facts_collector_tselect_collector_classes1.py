
import pytest
from ansible.module_utils.facts.collector import select_collector_classes

# Assuming these are defined elsewhere in your codebase
class CollectorClassA: pass
class CollectorClassB: pass
class CollectorClassC: pass
class CollectorClassD: pass  # Added for testing non-existent collector

def test_empty_all_fact_subsets():
    collector_names = ['collector1']
    all_fact_subsets = {}
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert selected_classes == []

def test_non_existent_collectors():
    collector_names = ['collector1', 'collector4']  # 'collector4' does not exist
    all_fact_subsets = {
        'collector1': [CollectorClassA, CollectorClassB],
        'collector2': [CollectorClassB, CollectorClassC]
    }
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {CollectorClassA, CollectorClassB}

def test_duplicate_within_same_collector():
    collector_names = ['collector1']
    all_fact_subsets = {
        'collector1': [CollectorClassA, CollectorClassB, CollectorClassB]  # Duplicate within the same collector
    }
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {CollectorClassA, CollectorClassB}

def test_all_collectors_have_duplicate_classes():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [CollectorClassA, CollectorClassB],
        'collector2': [CollectorClassB, CollectorClassC]
    }
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {CollectorClassA, CollectorClassB, CollectorClassC}
