# Module: ansible.utils.singleton
import pytest
from threading import RLock
from ansible.utils.singletonclass import Singleton

# Define a class using the Singleton metaclass
class MySingleton(metaclass=Singleton):
    def __init__(self, value):
        self.value = value

def test_singleton():
    # Create instances of MySingleton in different threads
    def create_instance():
        instance = MySingleton('foo')
        print(f"Instance created with value: {instance.value}")

    thread1 = threading.Thread(target=create_instance)
    thread2 = threading.Thread(target=create_instance)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Check that both threads created the same instance
    assert MySingleton('foo') is MySingleton('bar')
