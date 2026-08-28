
import pytest
from flutes.structure import no_map_instance, _NO_MAP_INSTANCE_ATTR

def test_edge_case_none():
    instance = None
    with pytest.raises(TypeError):
        no_map_instance(instance)



def test_invalid_case_bool():
    instance = True
    with pytest.raises(TypeError):
        no_map_instance(instance)


def test_valid_case_list():
    instance = [1, 2, 3]
    result = no_map_instance(instance)
    assert hasattr(result, _NO_MAP_INSTANCE_ATTR) is True

def test_valid_case_dict():
    instance = {'a': 1, 'b': 2}
    result = no_map_instance(instance)
    assert hasattr(result, _NO_MAP_INSTANCE_ATTR) is True

def test_valid_case_tuple():
    instance = (1, 2, 3)
    result = no_map_instance(instance)
    assert isinstance(result, tuple)
    assert hasattr(result, _NO_MAP_INSTANCE_ATTR) is True

def test_valid_case_custom_class():
    class MyClass:
        def __init__(self, value):
            self.value = value

    instance = MyClass(10)
    result = no_map_instance(instance)
    assert hasattr(result, _NO_MAP_INSTANCE_ATTR) is True