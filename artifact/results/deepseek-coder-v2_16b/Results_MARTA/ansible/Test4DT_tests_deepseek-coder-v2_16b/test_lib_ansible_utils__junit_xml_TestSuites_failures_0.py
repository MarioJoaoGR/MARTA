
import pytest
from ansible.utils._junit_xml import TestSuite, TestSuites
import decimal

# Scenario 1: Instantiating an Empty TestSuites Object
@pytest.fixture
def empty_test_suites():
    return TestSuites()

def test_empty_test_suites(empty_test_suites):
    assert empty_test_suites.name is None
    assert len(empty_test_suites.suites) == 0

# Scenario 2: Adding Suites to a TestSuites Object and Calculating Failures
@pytest.fixture
def populated_test_suites():
    suite1 = TestSuite(name="Suite 1", failures=3, time=decimal.Decimal('10'))
    suite2 = TestSuite(name="Suite 2", failures=2, time=decimal.Decimal('20'))
    test_suites = TestSuites()
    test_suites.suites.extend([suite1, suite2])
    return test_suites


# Scenario 3: Converting to XML and Pretty Printing (Assuming _pretty_xml function exists)

# Scenario 4: Instantiating with a Name
@pytest.fixture
def named_test_suites():
    return TestSuites(name="My Test Suites")

def test_named_test_suites(named_test_suites):
    assert named_test_suites.name == "My Test Suites"