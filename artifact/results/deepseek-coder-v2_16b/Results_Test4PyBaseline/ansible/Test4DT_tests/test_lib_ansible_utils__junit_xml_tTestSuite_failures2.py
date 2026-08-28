
import pytest
from ansible.utils._junit_xml import TestSuite, TestCase

# Initialization with Optional Parameters
def test_initialization_with_optional_parameters():
    suite = TestSuite(name="Example Suite", hostname="localhost", id="12345")
    assert suite.name == "Example Suite"
    assert suite.hostname == "localhost"
    assert suite.id == "12345"
    assert suite.package is None
    assert suite.timestamp is None
    assert suite.properties == {}
    assert suite.cases == []
    assert suite.system_out is None
    assert suite.system_err is None

# Adding Test Cases
def test_adding_test_cases():
    suite = TestSuite(name="Example Suite")
    case1 = TestCase(name="Test Case 1", status="failed")
    case2 = TestCase(name="Test Case 2", status="passed")
    suite.cases.extend([case1, case2])
    assert len(suite.cases) == 2

# Test Cases for Failures Calculation
def test_failures_calculation():
    suite = TestSuite(name="Example Suite")
    # No failures initially