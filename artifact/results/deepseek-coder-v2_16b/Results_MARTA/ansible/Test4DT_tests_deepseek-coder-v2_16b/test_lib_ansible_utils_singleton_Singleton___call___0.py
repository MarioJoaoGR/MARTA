
import pytest
from ansible.utils.singleton import Singleton

def test_singleton_instance():
    class MySingleton(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

    instance1 = MySingleton(10)
    instance2 = MySingleton(20)  # This should return the same instance as instance1

    assert instance1 is instance2
    assert instance1.value == 10
    assert instance2.value == 10

def test_singleton_method():
    class MySingleton(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    instance1 = MySingleton(10)
    instance2 = MySingleton(20)  # This should return the same instance as instance1

    assert instance1.get_value() == 10
    assert instance2.get_value() == 10
