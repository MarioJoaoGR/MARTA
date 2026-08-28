
import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import build_fact_id_to_collector_map

# Helper class for creating collector classes
class CollectorClass:
    def __init__(self, name, fact_ids):
        self.name = name
        self._fact_ids = fact_ids  # Using a protected attribute to mimic the internal nature of the fact_ids list

def test_build_fact_id_to_collector_map_basic():
    collectors = [
        CollectorClass(name='collector1', fact_ids=['fact1', 'alias1']),
        CollectorClass(name='collector2', fact_ids=['fact2'])
    ]

    result = build_fact_id_to_collector_map(collectors)
    assert isinstance(result, tuple), "The function should return a tuple"
    assert len(result) == 2, "The tuple should contain two elements"
    
    fact_id_to_collector_map, aliases_map = result
    assert isinstance(fact_id_to_collector_map, defaultdict), "First element should be a defaultdict"
    assert isinstance(aliases_map, defaultdict), "Second element should be a defaultdict"
    
    # Check fact_id_to_collector_map
    assert 'collector1' in fact_id_to_collector_map
    assert len(fact_id_to_collector_map['collector1']) == 1
    assert isinstance(fact_id_to_collector_map['collector1'][0], CollectorClass)
    
    assert 'fact1' in fact_id_to_collector_map