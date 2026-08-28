
import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import build_dep_data

# Test cases for build_dep_data function
def test_build_dep_data_basic():
    collectors = ['collector1', 'collector2']
    all_facts = {
        'collector1': [{'fact1'}, {'fact2'}],
        'collector2': [{'fact3'}, {'fact4'}]
    }
    expected_output = {
        'collector1': {'fact1', 'fact2'},
        'collector2': {'fact3', 'fact4'}
    }
    assert build_dep_data(collectors, all_facts) == expected_output

def test_build_dep_data_empty():
    empty_collectors = []
    empty_all_facts = {}
    assert build_dep_data(empty_collectors, empty_all_facts) == {}

def test_build_dep_data_different_fact_structures():
    collectors = ['collectorA', 'collectorB']
    all_facts = {
        'collectorA': [{'factA1'}, {'factA2'}],
        'collectorB': [{'factB1'}, {'factB2'}]
    }
    expected_output = {
        'collectorA': {'factA1', 'factA2'},
        'collectorB': {'factB1', 'factB2'}
    }
    assert build_dep_data(collectors, all_facts) == expected_output

def test_build_dep_data_single_collector():
    collectors = ['singleCollector']
    all_facts = {
        'singleCollector': [{'fact1'}, {'fact2'}]
    }
    expected_output = {
        'singleCollector': {'fact1', 'fact2'}
    }
    assert build_dep_data(collectors, all_facts) == expected_output

def test_build_dep_data_custom_fact_objects():
    class CustomFact:
        def __init__(self, name):
            self.required_facts = {name}

    collectors = ['customCollector']
    all_facts = {
        'customCollector': [CustomFact('customFact1'), CustomFact('customFact2')]
    }
    expected_output = {
        'customCollector': {'customFact1', 'customFact2'}
    }
    assert build_dep_data(collectors, all_facts) == expected_output
