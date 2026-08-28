
import pytest
from collections import defaultdict

# Define a custom exception for cycle detection
class CycleFoundInFactDeps(Exception):
    pass

def tsort(dep_map):
    sorted_list = []
    unsorted_map = dep_map.copy()

    while unsorted_map:
        acyclic = False
        for node, edges in list(unsorted_map.items()):
            for edge in edges:
                if edge in unsorted_map:
                    break
            else:
                acyclic = True
                del unsorted_map[node]
                sorted_list.append((node, edges))

        if not acyclic:
            raise CycleFoundInFactDeps('Unable to tsort deps, there was a cycle in the graph. sorted=%s' % sorted_list)

    return sorted_list

# Test scenarios
def test_valid_input():
    dep_map = {'A': ['B'], 'B': [], 'C': ['A']}
    expected_output = [('B', []), ('A', ['B']), ('C', ['A'])]
    assert tsort(dep_map) == expected_output

def test_cycle_detection():
    dep_map = {'A': ['B'], 'B': ['C'], 'C': ['A']}
    with pytest.raises(CycleFoundInFactDeps):
        tsort(dep_map)

def test_empty_input():
    dep_map = {}
    expected_output = []
    assert tsort(dep_map) == expected_output
