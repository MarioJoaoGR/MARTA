
import pytest
from unittest.mock import patch, MagicMock
import xml.etree.ElementTree as ET
import decimal
from dataclasses import dataclass
import typing as t

@dataclass
class TestSuite:
    name: str
    disabled: int = 0
    errors: int = 0
    failures: int = 0
    tests: int = 0
    time: decimal.Decimal = decimal.Decimal('0')

class TestSuites:
    'A collection of test suites.'
    name: t.Optional[str] = None
    suites: t.List[TestSuite] = dataclasses.field(default_factory=list)

    def time(self) -> decimal.Decimal:
        return sum(suite.time for suite in self.suites)

def test_total_time():
    ts = TestSuites()
    suite1 = TestSuite(name="Suite 1", time=decimal.Decimal('10'))
    suite2 = TestSuite(name="Suite 2", time=decimal.Decimal('20'))
    ts.suites.extend([suite1, suite2])
    
    assert ts.time() == decimal.Decimal('30')

def test_total_time_with_different_times():
    ts = TestSuites()
    suite1 = TestSuite(name="Suite 1", time=decimal.Decimal('5'))
    suite2 = TestSuite(name="Suite 2", time=decimal.Decimal('15'))
    ts.suites.extend([suite1, suite2])
    
    assert ts.time() == decimal.Decimal('20')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_lib_ansible_utils__junit_xml_TestSuites_time_0.py ____
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py:18: in <module>
    class TestSuites:
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py:21: in TestSuites
    suites: t.List[TestSuite] = dataclasses.field(default_factory=list)
E   NameError: name 'dataclasses' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.34s ===============================
"""