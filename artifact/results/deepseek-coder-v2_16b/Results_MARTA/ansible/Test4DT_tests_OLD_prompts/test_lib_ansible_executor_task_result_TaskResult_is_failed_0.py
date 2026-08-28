
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.executor.task_result import TaskResult

# Test Scenario 1: Test standard input with valid data to ensure is_failed method returns correct result
def test_valid_input_happy_path():
    return_data = {'results': [{'failed_when_result': False}, {'failed_when_result': True}]}
    task_result = TaskResult(host='localhost', task='update_packages', return_data=return_data)
    assert task_result.is_failed() == True  # Ensure this is the correct assertion based on your logic

# Test Scenario 2: Test edge case where input data is None to check error handling
def test_edge_case_none():
    return_data = None
    with pytest.raises(TypeError):
        TaskResult(host='localhost', task='update_packages', return_data=return_data)

# Test Scenario 3: Test invalid input where return_data is not a dictionary or string, ensuring error handling kicks in
def test_invalid_input_error_handling():
    return_data = 12345  # Unsupported type
    with pytest.raises(TypeError):
        TaskResult(host='localhost', task='update_packages', return_data=return_data)
