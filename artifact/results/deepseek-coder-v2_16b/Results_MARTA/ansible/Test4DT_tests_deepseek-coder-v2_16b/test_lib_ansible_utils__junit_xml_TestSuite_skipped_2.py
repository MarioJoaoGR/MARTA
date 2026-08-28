
import pytest
from datetime import datetime
import dataclasses
import typing as t
from unittest.mock import patch, MagicMock

# Assuming TestCase is defined elsewhere in your codebase or imported from a module
@dataclasses.dataclass
class TestCase:
    name: str
    is_skipped: bool = False
    is_error: bool = False

@dataclasses.dataclass
class TestSuite:
    'A collection of test cases.'
    name: str
    hostname: t.Optional[str] = None
    id: t.Optional[str] = None
    package: t.Optional[str] = None
    timestamp: t.Optional[datetime] = None
    properties: t.Dict[str, str] = dataclasses.field(default_factory=dict)
    cases: t.List[TestCase] = dataclasses.field(default_factory=list)
    system_out: t.Optional[str] = None
    system_err: t.Optional[str] = None

    def skipped(self) -> int:
        """Returns the total number of test cases that have been marked as skipped."""
        return sum(case.is_skipped for case in self.cases)

# Test Suite Definition
@pytest.fixture
def valid_suite():
    return TestSuite(name="Example Suite")

@pytest.fixture
def edge_case_suite():
    suite = TestSuite(name="Edge Case Suite", hostname="localhost", id="12345", package="example_package", timestamp=datetime.now(), properties={"env": "test"})
    case1 = TestCase(name="Test Case 1")
    case2 = TestCase(name="Test Case 2", is_skipped=True)
    suite.cases.extend([case1, case2])
    return suite

@pytest.fixture
def invalid_suite():
    with pytest.raises(TypeError):
        TestSuite()

# Test Functions
def test_valid_inputs(valid_suite):
    assert valid_suite.name == "Example Suite"
    assert valid_suite.skipped() == 0

def test_edge_cases(edge_case_suite):
    assert edge_case_suite.name == "Edge Case Suite"
    assert edge_case_suite.hostname == "localhost"
    assert edge_case_suite.id == "12345"
    assert edge_case_suite.package == "example_package"
    assert len(edge_case_suite.cases) == 2
    assert edge_case_suite.skipped() == 1

def test_invalid_inputs():
    with pytest.raises(TypeError):
        TestSuite()
