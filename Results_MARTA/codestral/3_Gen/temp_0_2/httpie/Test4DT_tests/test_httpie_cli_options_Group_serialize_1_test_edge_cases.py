
import pytest
from unittest.mock import patch
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Argument:
    name: str
    value: any
    
    def serialize(self) -> Dict[str, Any]:
        return {'name': self.name, 'value': self.value}

@dataclass
class Group:
    name: str
    description: str = ''
    is_mutually_exclusive: bool = False
    arguments: List['Argument'] = field(default_factory=list)
    
    def serialize(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description or None,
            'is_mutually_exclusive': self.is_mutually_exclusive,
            'args': [argument.serialize() for argument in self.arguments],
        }

def test_edge_cases():
    # Test with None name
    group_none = Group(name=None, description='', is_mutually_exclusive=False, arguments=[])
    assert group_none.serialize() == {'name': None, 'description': None, 'is_mutually_exclusive': False, 'args': []}
    
    # Test with empty list of arguments
    group_empty_list = Group(name='example_group', description='This is an example group', is_mutually_exclusive=True, arguments=[])
    assert group_empty_list.serialize() == {'name': 'example_group', 'description': 'This is an example group', 'is_mutually_exclusive': True, 'args': []}
    
    # Test with boundary values (non-empty list of arguments)
    arg1 = Argument(name='arg1', value=1)
    arg2 = Argument(name='arg2', value=2)
    group_boundary = Group(name='example_group', description='This is an example group', is_mutually_exclusive=True, arguments=[arg1, arg2])
    assert group_boundary.serialize() == {'name': 'example_group', 'description': 'This is an example group', 'is_mutually_exclusive': True, 'args': [{'name': 'arg1', 'value': 1}, {'name': 'arg2', 'value': 2}]}
