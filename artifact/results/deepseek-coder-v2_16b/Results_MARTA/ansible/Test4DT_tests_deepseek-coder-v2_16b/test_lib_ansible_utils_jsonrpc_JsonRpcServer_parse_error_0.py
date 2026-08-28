
import pytest
from lib.ansible.utils.jsonrpc import JsonRpcServer

# Test scenarios for parse_error method in JsonRpcServer class

@pytest.fixture(scope="module")
def server():
    return JsonRpcServer()

# Scenario 1: Test parse_error with valid data
def test_parse_error_with_valid_data(server):
    # Arrange (setup) is handled by the fixture
    # Act
    error_response = server.parse_error({"key": "value"})
    # Assert
    assert isinstance(error_response, dict), "Expected a dictionary response"
    assert error_response["code"] == -32700, "Expected specific error code"
    assert error_response["message"] == "Parse error", "Expected specific error message"
    assert error_response.get("data") is not None, "Expected data to be included in the response"

# Scenario 2: Test parse_error without additional data
def test_parse_error_without_data(server):
    # Arrange (setup) is handled by the fixture
    # Act
    error_response = server.parse_error()
    # Assert
    assert isinstance(error_response, dict), "Expected a dictionary response"
    assert error_response["code"] == -32700, "Expected specific error code"
    assert error_response["message"] == "Parse error", "Expected specific error message"
    assert error_response.get("data") is None, "Expected no data in the response"

# Scenario 3: Test parse_error with invalid input format
def test_parse_error_with_invalid_input(server):
    # Arrange (setup) is handled by the fixture
    # Act
    error_response = server.parse_error("not a dictionary")
    # Assert
    assert isinstance(error_response, dict), "Expected a dictionary response"
    assert error_response["code"] == -32700, "Expected specific error code"
    assert error_response["message"] == "Parse error", "Expected specific error message"
    assert error_response.get("data") is None, "Expected no data in the response"
