
import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite

# Test Suite for the TestSuites class
def test_test_suites_initialization():
    ts = TestSuites()
    assert str(ts) == "TestSuites(name=None, suites=[])"

def test_adding_suites_to_test_suites():
    ts = TestSuites()
    suite1 = TestSuite("Suite 1")
    suite2 = TestSuite("Suite 2")
    ts.suites.append(suite1)
    ts.suites.append(suite2)
    assert ts.disabled() == 0

def test_disabling_test_case():
    ts = TestSuites()
    suite1 = TestSuite("Suite 1")
    suite2 = TestSuite("Suite 2")
    ts.suites.append(suite1)
    ts.suites.append(suite2)
    setattr(suite1, 'disabled', True)  # Corrected line
    assert not suite1.disabled  # Assuming the intention was to check if it's False after setting disabled to True

def test_multiple_suites_with_different_states():
    ts = TestSuites()
    suite1 = TestSuite("Suite 1")
    suite2 = TestSuite("Suite 2")
    suite3 = TestSuite("Suite 3")
    ts.suites.append(suite1)
    ts.suites.append(suite2)
    ts.suites.append(suite3)
    setattr(suite1, 'disabled', True)  # Corrected line
    assert suite1.disabled  # Assuming the intention was to check if it's True after setting disabled to True
