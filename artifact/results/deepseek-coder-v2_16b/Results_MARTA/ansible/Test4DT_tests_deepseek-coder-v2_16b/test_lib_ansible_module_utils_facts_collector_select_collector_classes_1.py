
import pytest
from ansible.module_utils.facts.collector import select_collector_classes

# Define some dummy classes for testing
class ClassA: pass
class ClassB: pass
class ClassC: pass
class ClassD: pass
class ClassE: pass
class ClassF: pass
class ClassG: pass
class ClassH: pass
class ClassI: pass
class ClassJ: pass
class ClassK: pass
class ClassL: pass

def test_valid_input_multiple_collectors():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [ClassA, ClassB],
        'collector2': [ClassC, ClassD]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {ClassA, ClassB, ClassC, ClassD}

def test_valid_input_one_collector():
    collector_names = ['collector1']
    all_fact_subsets = {
        'collector1': [ClassE, ClassF],
        'collector2': [ClassG, ClassH]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {ClassE, ClassF}

def test_valid_input_non_existent_collector():
    collector_names = ['non_existent_collector']
    all_fact_subsets = {
        'collector1': [ClassI, ClassJ],
        'collector2': [ClassK, ClassL]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert not selected_classes
