
import pytest
from datetime import datetime
import typing as t
import dataclasses
from unittest.mock import patch, MagicMock

# Assuming TestSuite and TestCase are defined elsewhere in your codebase
class TestCase:
    def __init__(self, name: str, is_skipped=False):
        self.name = name
        self.is_skipped = is_skipped

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

# Test Suite for valid inputs
def test_valid_inputs():
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

# Test Suite for edge cases
def test_edge_cases():
    suite = TestSuite(name="Edge Case Suite")
    suite.cases.append(TestCase(name="Edge Case 1"))
    suite.cases.append(TestCase(name="Edge Case 2", is_skipped=True))
    
    assert suite.name == "Edge Case Suite"
    assert suite.hostname is None
    assert suite.id is None
    assert suite.package is None
    assert suite.timestamp is None
    assert suite.properties == {}
    assert len(suite.cases) == 2
    assert suite.skipped() == 1

# Test Suite for invalid inputs and error handling
def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the constructor expects at least one argument (name)
        suite = TestSuite()
