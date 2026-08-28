
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterError

# Test cases for the unique function
def test_unique_basic():
    environment = {'var': 'value'}
    assert mathstuff.unique(environment, ['apple', 'banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']

def test_unique_case_sensitive():
    environment = {'var': 'value'}
    assert mathstuff.unique(environment, ['Apple', 'Banana', 'apple', 'Cherry'], case_sensitive=True) == ['Apple', 'Banana', 'apple', 'Cherry']

def test_unique_attribute():
    environment = {'var': 'value'}
    data = [{'id': 1}, {'id': 2}, {'id': 1}]