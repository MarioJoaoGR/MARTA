
import pytest
from datetime import datetime
from unittest.mock import patch
from ansible.utils._junit_xml import TestSuite, TestCase

# Basic Initialization
def test_basic_initialization():
    suite = TestSuite(name="Example Suite")
    assert suite.name == "Example Suite"
    assert suite.hostname is None
    assert suite.id is None
    assert suite.package is None
    assert suite.timestamp is None
    assert suite.properties == {}
    assert suite.cases == []
    assert suite.system_out is None
    assert suite.system_err is None

# Initialization with Optional Parameters
def test_initialization_with_optional_parameters():
    suite = TestSuite(name="Example Suite", hostname="localhost", id="suite123", package="example_package", timestamp=datetime.now())
    assert suite.name == "Example Suite"
    assert suite.hostname == "localhost"
    assert suite.id == "suite123"
    assert suite.package == "example_package"
    assert isinstance(suite.timestamp, datetime)
    assert suite.properties == {}
    assert suite.cases == []
    assert suite.system_out is None
    assert suite.system_err is None

# Adding Test Cases
def test_adding_test_cases():
    suite = TestSuite(name="Example Suite")
    case1 = TestCase(name="Test Case 1")
    case2 = TestCase(name="Test Case 2")
    suite.cases.extend([case1, case2])
    assert len(suite.cases) == 2