
import pytest
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
    group_empty = Group(name='empty_group', description='', is_mutually_exclusive=False, arguments=[])
    
    expected_output = {
        'name': 'empty_group',
        'description': None,
        'is_mutually_exclusive': False,
        'args': []
    }
    
    assert group_empty.serialize() == expected_output
