
import pytest
from ansible.module_utils.facts.collector import select_collector_classes

# Assuming these are defined elsewhere in your codebase
class CollectorClassA: pass
class CollectorClassB: pass
class CollectorClassC: pass

# Test cases for select_collector_classes function

def test_basic_usage():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [CollectorClassA, CollectorClassB],
        'collector2': [CollectorClassB, CollectorClassC]
    }
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {CollectorClassA, CollectorClassB, CollectorClassC}

def test_empty_input():
    collector_names = []
    all_fact_subsets = {}
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert selected_classes == []

def test_single_collector_name():
    collector_names = ['collector1']
    all_fact_subsets = {
        'collector1': [CollectorClassA, CollectorClassB]
    }
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {CollectorClassA, CollectorClassB}

def test_duplicate_collectors():
    collector_names = ['collector1', 'collector1']
    all_fact_subsets = {
        'collector1': [CollectorClassA, CollectorClassB]
    }
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {CollectorClassA, CollectorClassB}

def test_all_collectors_have_duplicate_classes():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [CollectorClassA],
        'collector2': [CollectorClassA]
    }
    
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)