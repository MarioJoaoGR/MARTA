
import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import build_fact_id_to_collector_map

# Helper class for creating collector classes
class CollectorClass:
    def __init__(self, name, fact_ids):
        self.name = name
        self._fact_ids = fact_ids  # Using a protected attribute to mimic the internal nature of the fact_ids list

def test_build_fact_id_to_collector_map_empty():
    collectors = []
    result = build_fact_id_to_collector_map(collectors)
    assert isinstance(result, tuple), "The function should return a tuple"
    assert len(result) == 2, "The tuple should contain two elements"
    
    fact_id_to_collector_map, aliases_map = result
    assert isinstance(fact_id_to_collector_map, defaultdict), "First element should be a defaultdict"
    assert isinstance(aliases_map, defaultdict), "Second element should be a defaultdict"
    assert len(fact_id_to_collector_map) == 0, "The fact_id_to_collector_map should be empty"
    assert len(aliases_map) == 0, "The aliases_map should be empty"

def test_build_fact_id_to_collector_map_single():
    collectors = [CollectorClass(name='collector1', fact_ids=['fact1'])]
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
    
    # Check aliases_map
    assert 'collector1' in aliases_map
    assert len(aliases_map['collector1']) == 1
    assert 'fact1' in aliases_map['collector1']

def test_build_fact_id_to_collector_map_multiple():
    collectors = [
        CollectorClass(name='collector1', fact_ids=['fact1']),
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
    
    assert 'collector2' in fact_id_to_collector_map
    assert len(fact_id_to_collector_map['collector2']) == 1
    assert isinstance(fact_id_to_collector_map['collector2'][0], CollectorClass)
    
    # Check aliases_map
    assert 'collector1' in aliases_map
    assert len(aliases_map['collector1']) == 1
    assert 'fact1' in aliases_map['collector1']
    
    assert 'collector2' in aliases_map
    assert len(aliases_map['collector2']) == 1
    assert 'fact2' in aliases_map['collector2']

def test_build_fact_id_to_collector_map_with_aliases():
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
    
    assert 'alias1' in fact_id_to_collector_map
    assert len(fact_id_to_collector_map['alias1']) == 1
    assert isinstance(fact_id_to_collector_map['alias1'][0], CollectorClass)
    
    # Check aliases_map
    assert 'collector1' in aliases_map
    assert len(aliases_map['collector1']) == 2
    assert 'fact1' in aliases_map['collector1']
    assert 'alias1' in aliases_map['collector1']
    
    # Check fact_id_to_collector_map for fact2
    assert 'collector2' in fact_id_to_collector_map
    assert len(fact_id_to_collector_map['collector2']) == 1
    assert isinstance(fact_id_to_collector_map['collector2'][0], CollectorClass)
    
    # Check aliases_map for collector2
    assert 'collector2' in aliases_map
    assert len(aliases_map['collector2']) == 1
    assert 'fact2' in aliases_map['collector2']
