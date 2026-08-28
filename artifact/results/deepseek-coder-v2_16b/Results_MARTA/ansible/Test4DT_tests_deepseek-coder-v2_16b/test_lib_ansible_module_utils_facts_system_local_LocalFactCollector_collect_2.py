
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.module_utils.facts.system.localclass import LocalFactCollector
import os
import glob
import stat
import json
import configparser
from io import StringIO

# Test data setup
@pytest.fixture
def module_with_valid_fact_path():
    class ModuleMock:
        def __init__(self, params):
            self.params = params
        
        def params(self):
            return {'fact_path': '/valid/path/to/facts'}
        
        def warn(self, message):
            print(f"Warning: {message}")
        
        def run_command(self, command):
            if command.endswith('.fact'):
                return (0, "{}", "")  # Successful execution with empty JSON content
            else:
                raise FileNotFoundError("Command not found")

    module = ModuleMock({'fact_path': '/valid/path/to/facts'})
    return module

@pytest.fixture
def module_without_module():
    class ModuleMock:
        def params(self):
            return {}
        
        def warn(self, message):
            print(f"Warning: {message}")
        
        def run_command(self, command):
            raise FileNotFoundError("Module not provided")

    module = ModuleMock()
    return module

@pytest.fixture
def module_with_invalid_fact_path():
    class ModuleMock:
        def __init__(self, params):
            self.params = params
        
        def params(self):
            return {'fact_path': '/nonexistent/path'}
        
        def warn(self, message):
            print(f"Warning: {message}")
        
        def run_command(self, command):
            if command.endswith('.fact'):
                return (0, "{}", "")  # Successful execution with empty JSON content
            else:
                raise FileNotFoundError("Command not found")

    module = ModuleMock({'fact_path': '/nonexistent/path'})
    return module

# Test functions
def test_valid_input(module_with_valid_fact_path):
    collector = LocalFactCollector()
    result = collector.collect(module=module_with_valid_fact_path)
    assert isinstance(result, dict), "Expected a dictionary"
    assert 'local' in result, "Expected key 'local' in the result"
    assert len(result['local']) > 0, "Expected non-empty local facts"

def test_missing_module(module_without_module):
    collector = LocalFactCollector()
    result = collector.collect(module=module_without_module)
    assert isinstance(result, dict), "Expected a dictionary"
    assert 'local' in result, "Expected key 'local' in the result"
    assert len(result['local']) == 0, "Expected empty local facts when no module is provided"

def test_invalid_fact_path(module_with_invalid_fact_path):
    collector = LocalFactCollector()
    result = collector.collect(module=module_with_invalid_fact_path)
    assert isinstance(result, dict), "Expected a dictionary"
    assert 'local' in result, "Expected key 'local' in the result"
    assert len(result['local']) == 0, "Expected empty local facts when fact path does not exist"
