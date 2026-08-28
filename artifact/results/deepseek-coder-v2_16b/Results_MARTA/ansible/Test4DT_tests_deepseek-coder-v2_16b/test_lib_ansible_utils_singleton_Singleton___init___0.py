
import pytest
from ansible.utils.singleton import Singleton
from threading import RLock


def test_valid_creation():
    """Test that creating instances of a class using Singleton metaclass results in the same instance being returned each time."""
    class ValidSingleton(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

    instance1 = ValidSingleton('A')
    instance2 = ValidSingleton('B')  # Both instances will reference the same object

    assert instance1 is instance2
    assert instance1.value == 'A'
    assert instance2.value == 'A'

def test_accessing_attribute():
    """Test that accessing an attribute of a singleton instance works correctly."""
    class ValidSingleton(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

    instance1 = ValidSingleton('A')
    assert instance1.value == 'A'