
import pytest
from ansible.inventory.helpers import sort_groups

class Group:
    def __init__(self, depth, priority, name):
        self.depth = depth
        self.priority = priority
        self.name = name

def test_sort_groups_valid():
    groups_list = [Group(1, 2, 'groupC'), Group(2, 1, 'groupA'), Group(1, 1, 'groupB')]
    sorted_groups = sort_groups(groups_list)
    assert len(sorted_groups) == 3
    assert sorted_groups[0].depth == 1 and sorted_groups[0].priority == 1 and sorted_groups[0].name == 'groupB'
    assert sorted_groups[1].depth == 1 and sorted_groups[1].priority == 2 and sorted_groups[1].name == 'groupC'
    assert sorted_groups[2].depth == 2 and sorted_groups[2].priority == 1 and sorted_groups[2].name == 'groupA'

def test_sort_groups_equal_priorities():
    groups_list = [Group(1, 1, 'groupB'), Group(1, 1, 'groupC')]
    sorted_groups = sort_groups(groups_list)
    assert len(sorted_groups) == 2
    assert sorted_groups[0].depth == 1 and sorted_groups[0].priority == 1 and sorted_groups[0].name == 'groupB'
    assert sorted_groups[1].depth == 1 and sorted_groups[1].priority == 1 and sorted_groups[1].name == 'groupC'
