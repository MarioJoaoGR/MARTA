
import pytest

class CommonVariable:
    def _get_value(self, main_value, key):
        raise NotImplementedError

class MyVariable(CommonVariable):
    def _get_value(self, main_value, key):
        return main_value.get(key)

class ListVariable(CommonVariable):
    def _get_value(self, main_value, key):
        return main_value[key]

class ObjectVariable(CommonVariable):
    def _get_value(self, main_value, key):
        return getattr(main_value, key)

class MyObject:
    def __init__(self):
        self.x = 5
        self.y = 10

def test_valid_case_dict():
    my_var = MyVariable()
    main_value = {'a': 1, 'b': 2}
    key = 'a'
    assert my_var._get_value(main_value, key) == 1

def test_valid_case_list():
    list_var = ListVariable()
    main_value = [10, 20, 30]
    key = 1
    assert list_var._get_value(main_value, key) == 20

def test_valid_case_object():
    obj_var = ObjectVariable()
    my_obj = MyObject()
    main_value = my_obj
    key = 'x'
    assert obj_var._get_value(main_value, key) == 5

def test_edge_case_none_main_value():
    my_var = MyVariable()
    main_value = None
    key = 'a'
    with pytest.raises(AttributeError):
        my_var._get_value(main_value, key)

def test_edge_case_empty_dict():
    my_var = MyVariable()
    main_value = {}
    key = 'a'
    assert my_var._get_value(main_value, key) is None

def test_edge_case_empty_list():
    list_var = ListVariable()
    main_value = []
    key = 0
    with pytest.raises(IndexError):
        list_var._get_value(main_value, key)

def test_invalid_key_dict():
    my_var = MyVariable()
    main_value = {'a': 1, 'b': 2}
    key = 'c'
    assert my_var._get_value(main_value, key) is None

def test_invalid_key_list():
    list_var = ListVariable()
    main_value = [10, 20, 30]
    key = 5
    with pytest.raises(IndexError):
        list_var._get_value(main_value, key)

def test_invalid_key_object():
    obj_var = ObjectVariable()
    my_obj = MyObject()
    main_value = my_obj
    key = 'z'
    with pytest.raises(AttributeError):
        obj_var._get_value(main_value, key)
