
import pytest
from collections import defaultdict

# Assuming the module under test is named 'collector_utils' and contains the function build_fact_id_to_collector_map
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

# Test scenarios
def test_valid_input():
    class CollectorA:
        name = 'CollectorA'
        fact_ids = ['fact1', 'fact2']

    class CollectorB:
        name = 'CollectorB'
        fact_ids = ['fact2', 'fact3']
    
    collectors = [CollectorA(), CollectorB()]
    result = build_fact_id_to_collector_map(collectors)
    
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Tuple should contain two elements"
    fact_id_to_collector_map, aliases_map = result
    
    assert isinstance(fact_id_to_collector_map, defaultdict), "First element should be a defaultdict"
    assert isinstance(aliases_map, defaultdict), "Second element should be a defaultdict"
    
    assert 'CollectorA' in fact_id_to_collector_map, "fact_id_to_collector_map should contain CollectorA"
    assert len(fact_id_to_collector_map['CollectorA']) == 1, "CollectorA should be listed once"
    
    assert 'fact1' in fact_id_to_collector_map, "fact_id_to_collector_map should contain fact1"
    assert len(fact_id_to_collector_map['fact1']) == 1, "fact1 should map to CollectorA"
    
    assert 'CollectorB' in fact_id_to_collector_map, "fact_id_to_collector_map should contain CollectorB"
    assert len(fact_id_to_collector_map['CollectorB']) == 1, "CollectorB should be listed once"
    
    assert 'fact2' in fact_id_to_collector_map, "fact_id_to_collector_map should contain fact2"
    assert len(fact_id_to_collector_map['fact2']) == 2, "fact2 should map to both CollectorA and CollectorB"
    
    assert 'fact3' in fact_id_to_collector_map, "fact_id_to_collector_map should contain fact3"
    assert len(fact_id_to_collector_map['fact3']) == 1, "fact3 should map to CollectorB"
    
    assert 'CollectorA' in aliases_map, "aliases_map should contain CollectorA"
    assert 'fact1' in aliases_map['CollectorA'], "CollectorA should have fact1 as an alias"
    assert 'fact2' in aliases_map['CollectorA'], "CollectorA should have fact2 as an alias"
    
    assert 'CollectorB' in aliases_map, "aliases_map should contain CollectorB"
    assert 'fact2' in aliases_map['CollectorB'], "CollectorB should have fact2 as an alias"
    assert 'fact3' in aliases_map['CollectorB'], "CollectorB should have fact3 as an alias"

def test_edge_case():
    collectors = None
    result = build_fact_id_to_collector_map(collectors)
    
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Tuple should contain two elements"
    fact_id_to_collector_map, aliases_map = result
    
    assert isinstance(fact_id_to_collector_map, defaultdict), "First element should be a defaultdict"
    assert isinstance(aliases_map, defaultdict), "Second element should be a defaultdict"
    
    assert len(fact_id_to_collector_map) == 0, "No fact IDs should be present if collectors is None"
    assert len(aliases_map) == 0, "No aliases should be present if collectors is None"

def test_invalid_input():
    collectors = 'InvalidInput'
    
    with pytest.raises(TypeError):
        build_fact_id_to_collector_map(collectors)
