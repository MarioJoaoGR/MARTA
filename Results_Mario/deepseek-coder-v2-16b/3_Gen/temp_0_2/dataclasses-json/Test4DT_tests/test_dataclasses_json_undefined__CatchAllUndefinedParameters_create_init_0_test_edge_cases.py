
import pytest
from dataclasses import dataclass, field
from typing import Callable
import inspect
import functools
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@pytest.fixture
def edge_case_class():
    @dataclass
    class EdgeCaseClass:
        y: list = field(default_factory=list)
    
    return EdgeCaseClass

def test_edge_cases(edge_case_class):
    # Create an instance of the dataclass with undefined parameters
    params = {}
    edge_instance = edge_case_class(**params)
    
    # Check that the list field is initialized correctly
    assert isinstance(edge_instance.y, list), "The 'y' field should be a list"
    assert edge_instance.y == [], "The 'y' field should be an empty list"
