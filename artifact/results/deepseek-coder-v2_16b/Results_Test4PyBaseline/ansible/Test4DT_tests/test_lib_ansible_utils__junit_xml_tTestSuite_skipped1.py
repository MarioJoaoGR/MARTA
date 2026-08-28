
import pytest
from ansible.utils._junit_xml import TestSuite, TestCase
from datetime import datetime

# Initialization with Optional Parameters
def test_initialization_with_optional_parameters():
    suite = TestSuite(name="Example Suite", hostname="localhost", id="suite123", package="example_package", timestamp=datetime.now())
    assert suite.name == "Example Suite"
    assert suite.hostname == "localhost"
    assert suite.id == "suite123"
    assert suite.package == "example_package"
    assert suite.timestamp is not None
    assert isinstance(suite.timestamp, datetime)
    assert suite.properties == {}
    assert suite.cases == []
    assert suite.system_out is None
    assert suite.system_err is None

# Adding Test Cases
def test_adding_test_cases():
    suite = TestSuite(name="Example Suite")
    case1 = TestCase(name="Test Case 1", status="passed")
    case2 = TestCase(name="Test Case 2", status="skipped")
    suite.cases.extend([case1, case2])
    assert len(suite.cases) == 2
    assert suite.cases[0].name == "Test Case 1"
    assert suite.cases[1].name == "Test Case 2"

# Checking the Number of Skipped Test Cases
def test_number_of_skipped_test_cases():
    suite = TestSuite(name="Example Suite")
    case1 = TestCase(name="Test Case 1", status="passed")
    case2 = TestCase(name="Test Case 2", status="skipped")
    suite.cases.extend([case1, case2])