
# Module: flutes.structure
import pytest
from flutes.structure import map_structure, register_no_map_class

def test_map_structure_no_map_types():
    # Define a custom class and register it in _NO_MAP_TYPES
    class CustomClass:
        def __init__(self, value):
            self.value = value
    
    register_no_map_class(CustomClass)
    
    obj = CustomClass(10)
    result = map_structure(lambda x: x * 2 if isinstance(x, int) else x, obj)
    assert result is obj  # The object should not be changed
    assert result.value == 10

def test_map_structure_no_map_instance_attr():
    # Define a custom class with the _NO_MAP_INSTANCE_ATTR attribute
    class CustomClass:
        _NO_MAP_INSTANCE_ATTR = True
        
        def __init__(self, value):
            self.value = value
    
    obj = CustomClass(20)
    result = map_structure(lambda x: x * 2 if isinstance(x, int) else x, obj)
    assert result is obj  # The object should not be changed
    assert result.value == 20

def test_map_structure_no_map_types_and_attr():
    # Define a custom class that is in _NO_MAP_TYPES and has the _NO_MAP_INSTANCE_ATTR attribute
    class CustomClass:
        _NO_MAP_INSTANCE_ATTR = True
        
        def __init__(self, value):
            self.value = value
    
    register_no_map_class(CustomClass)
    
    obj = CustomClass(30)
    result = map_structure(lambda x: x * 2 if isinstance(x, int) else x, obj)
    assert result is obj  # The object should not be changed
    assert result.value == 30

def test_map_structure_no_map_types_with_nested():
    # Define a custom class and register it in _NO_MAP_TYPES
    class CustomClass:
        def __init__(self, value):
            self.value = value
    
    register_no_map_class(CustomClass)
    
    obj = [CustomClass(10), {'key': CustomClass(20)}, (CustomClass(30),)]
    result = map_structure(lambda x: x * 2 if isinstance(x, int) else x, obj)
    assert isinstance(result[0], CustomClass)
    assert result[0].value == 10
    assert isinstance(result[1]['key'], CustomClass)
    assert result[1]['key'].value == 20
    assert isinstance(result[2][0], CustomClass)
    assert result[2][0].value == 30

def test_map_structure_no_map_instance_attr_with_nested():
    # Define a custom class with the _NO_MAP_INSTANCE_ATTR attribute
    class CustomClass:
        _NO_MAP_INSTANCE_ATTR = True
        
        def __init__(self, value):
            self.value = value
    
    obj = [CustomClass(10), {'key': CustomClass(20)}, (CustomClass(30),)]
    result = map_structure(lambda x: x * 2 if isinstance(x, int) else x, obj)
    assert isinstance(result[0], CustomClass)
    assert result[0].value == 10
    assert isinstance(result[1]['key'], CustomClass)
    assert result[1]['key'].value == 20
    assert isinstance(result[2][0], CustomClass)
    assert result[2][0].value == 30

def test_map_structure_no_map_types_and_attr_with_nested():
    # Define a custom class that is in _NO_MAP_TYPES and has the _NO_MAP_INSTANCE_ATTR attribute
    class CustomClass:
        _NO_MAP_INSTANCE_ATTR = True
        
        def __init__(self, value):
            self.value = value
    
    register_no_map_class(CustomClass)
    
    obj = [CustomClass(10), {'key': CustomClass(20)}, (CustomClass(30),)]
    result = map_structure(lambda x: x * 2 if isinstance(x, int) else x, obj)
    assert isinstance(result[0], CustomClass)
    assert result[0].value == 10
    assert isinstance(result[1]['key'], CustomClass)
    assert result[1]['key'].value == 20
    assert isinstance(result[2][0], CustomClass)
    assert result[2][0].value == 30
