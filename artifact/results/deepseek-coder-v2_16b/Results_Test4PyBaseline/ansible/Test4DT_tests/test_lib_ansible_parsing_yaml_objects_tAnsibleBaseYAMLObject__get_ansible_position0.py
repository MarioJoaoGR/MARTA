# Module: ansible.parsing.yaml.objects
import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

# Test case for creating an instance without any parameters
def test_create_instance_without_parameters():
    my_instance = AnsibleBaseYAMLObject()
    assert my_instance.ansible_pos == (None, 0, 0)

# Test case for creating a subclass and initializing it with specific position information
class MySubclass(AnsibleBaseYAMLObject):
    def __init__(self, data_source=None, line_number=0, column_number=0):
        self._data_source = data_source
        self._line_number = line_number
        self._column_number = column_number

def test_create_subclass_with_specific_position():
    my_instance = MySubclass("example.yaml", 10, 3)
    assert my_instance.ansible_pos == ("example.yaml", 10, 3)
