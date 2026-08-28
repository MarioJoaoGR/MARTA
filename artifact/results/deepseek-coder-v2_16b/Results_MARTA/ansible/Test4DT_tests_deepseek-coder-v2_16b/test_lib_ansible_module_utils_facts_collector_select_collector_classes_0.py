
import pytest
from ansible.module_utils.facts.collector import ClassA, ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassH, ClassI, ClassJ, ClassK, ClassL

def select_collector_classes(collector_names, all_fact_subsets):
    seen_collector_classes = set()
    selected_collector_classes = []
    for collector_name in collector_names:
        collector_classes = all_fact_subsets.get(collector_name, [])
        for collector_class in collector_classes:
            if collector_class not in seen_collector_classes:
                selected_collector_classes.append(collector_class)
                seen_collector_classes.add(collector_class)
    return selected_collector_classes

# Test scenarios
def test_valid_input():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [ClassA, ClassB],
        'collector2': [ClassC, ClassD]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {ClassA, ClassB, ClassC, ClassD}

def test_none_input():
    collector_names = None
    all_fact_subsets = {
        'collector1': [ClassE, ClassF],
        'collector2': [ClassG, ClassH]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert selected_classes == []

def test_empty_input():
    collector_names = []
    all_fact_subsets = {}
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert selected_classes == []
