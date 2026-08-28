
import pytest
from ansible.utils.singleton import Singleton
from unittest.mock import patch, MagicMock

# Scenario 1: Creating a class with the Singleton metaclass and ensuring only one instance is created
@pytest.mark.parametrize("value", ["A", "B"])
def test_singleton_instance(value):
    class MySingleton(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

    with patch('ansible.utils.singleton.RLock', MagicMock()):
        instance1 = MySingleton(value)
        instance2 = MySingleton(value)  # Both instances should reference the same object
        assert instance1 is instance2
        assert instance1.value == value
        assert instance2.value == value

# Scenario 2: Accessing an attribute of the singleton instance
@pytest.mark.parametrize("value", ["A", "B"])
def test_singleton_attribute(value):
    class MySingleton(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

    with patch('ansible.utils.singleton.RLock', MagicMock()):
        instance1 = MySingleton(value)
        assert instance1.value == value
