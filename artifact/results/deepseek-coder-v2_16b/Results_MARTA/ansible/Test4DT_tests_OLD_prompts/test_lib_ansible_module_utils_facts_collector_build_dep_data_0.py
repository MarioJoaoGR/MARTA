
import pytest
from ansible.module_utils.facts.collector import build_dep_data
from collections import defaultdict

# Define a mock for the required_facts attribute
class MockFactCollector:
    def __init__(self, facts):
        self.required_facts = set(facts)

def test_valid_inputs():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [MockFactCollector(['fact1']), MockFactCollector(['fact2'])],
        'collector2': [MockFactCollector(['fact3']), MockFactCollector(['fact4'])]
    }
    
    result = build_dep_data(collector_names, all_fact_subsets)
    
    assert result == {
        'collector1': {'fact1', 'fact2'},
        'collector2': {'fact3', 'fact4'}
    }
