
import pytest
from unittest.mock import patch
from ansible.executor.task_result import TaskResult, DataLoader

# Test initialization with dictionary return_data that does not contain 'changed' key
def test_init_with_dict_no_changed():
    host = "localhost"
    task = "fetch_data"
    return_data = {"status": "success", "data": {"key1": "value1"}}
    task_fields = {"user": "admin"}
    result = TaskResult(host, task, return_data, task_fields)
    
    assert not result.is_changed()

# Test initialization with string return_data that does not contain 'changed' key
def test_init_with_string_no_changed():
    host = "localhost"
    task = "fetch_data"
    return_data = '{"status": "success", "data": {"key1": "value1"}}'
    task_fields = {"user": "admin"}
    
    with patch('ansible.executor.task_result.DataLoader.load', return_value={"status": "success", "data": {"key1": "value1"}}):
        result = TaskResult(host, task, return_data, task_fields)
        
        assert not result.is_changed()

# Test initialization with dictionary return_data containing 'changed' key directly
def test_init_with_dict_contains_changed():
    host = "localhost"
    task = "fetch_data"
    return_data = {"status": "success", "changed": True, "data": {"key1": "value1"}}
    task_fields = {"user": "admin"}
    result = TaskResult(host, task, return_data, task_fields)
    
    assert result.is_changed()

# Test initialization with string return_data containing 'changed' key directly
def test_init_with_string_contains_changed():
    host = "localhost"
    task = "fetch_data"
    return_data = '{"status": "success", "changed": True, "data": {"key1": "value1"}}'
    task_fields = {"user": "admin"}
    
    with patch('ansible.executor.task_result.DataLoader.load', return_value={"status": "success", "changed": True, "data": {"key1": "value1"}}):
        result = TaskResult(host, task, return_data, task_fields)
        
        assert result.is_changed()

# Test initialization with dictionary return_data containing 'results' key with 'changed' entries
def test_init_with_dict_nested_contains_changed():
    host = "localhost"
    task = "fetch_data"
    return_data = {"status": "success", "results": [{"changed": True}, {"changed": False}]}
    task_fields = {"user": "admin"}
    result = TaskResult(host, task, return_data, task_fields)
    
    assert result.is_changed()

# Test initialization with string return_data containing 'results' key with 'changed' entries
def test_init_with_string_nested_contains_changed():
    host = "localhost"
    task = "fetch_data"
    return_data = '{"status": "success", "results": [{"changed": True}, {"changed": False}]}'
    task_fields = {"user": "admin"}
    
    with patch('ansible.executor.task_result.DataLoader.load', return_value={"status": "success", "results": [{"changed": True}, {"changed": False}]}):
        result = TaskResult(host, task, return_data, task_fields)
        
        assert result.is_changed()

# Test initialization with dictionary return_data containing 'failed' key instead of 'changed'
def test_init_with_dict_contains_failed():
    host = "localhost"
    task = "fetch_data"
    return_data = {"status": "success", "failed": True, "data": {"key1": "value1"}}
    task_fields = {"user": "admin"}
    result = TaskResult(host, task, return_data, task_fields)
    
    assert not result.is_changed()

# Test initialization with string return_data containing 'failed' key instead of 'changed'
def test_init_with_string_contains_failed():
    host = "localhost"
    task = "fetch_data"
    return_data = '{"status": "success", "failed": True, "data": {"key1": "value1"}}'
    task_fields = {"user": "admin"}
    
    with patch('ansible.executor.task_result.DataLoader.load', return_value={"status": "success", "failed": True, "data": {"key1": "value1"}}):
        result = TaskResult(host, task, return_data, task_fields)
        
        assert not result.is_changed()
