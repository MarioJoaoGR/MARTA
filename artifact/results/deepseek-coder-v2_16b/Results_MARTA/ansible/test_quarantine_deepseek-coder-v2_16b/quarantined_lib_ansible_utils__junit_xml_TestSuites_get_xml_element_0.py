
import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite
import xml.etree.ElementTree as ET



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_default_test_suites ___________________________

    def test_default_test_suites():
        test_suites = TestSuites()
        xml_element = test_suites.get_xml_element()
        assert xml_element.tag == 'testsuites'
>       assert xml_element.attrib['disabled'] == 'False'
E       AssertionError: assert '0' == 'False'
E         
E         - False
E         + 0

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py:10: AssertionError
_________________________ test_test_suites_with_suites _________________________

    def test_test_suites_with_suites():
        suite1 = TestSuite(name="Suite 1")
        suite2 = TestSuite(name="Suite 2")
        test_suites = TestSuites()
        test_suites.suites.extend([suite1, suite2])
        xml_element = test_suites.get_xml_element()
        assert xml_element.tag == 'testsuites'
        assert len(xml_element) == 2
        for i, suite in enumerate(test_suites.suites):
>           assert xml_element[i].tag == 'suite'
E           AssertionError: assert 'testsuite' == 'suite'
E             
E             - suite
E             + testsuite

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py:26: AssertionError
__________________________ test_test_suites_with_name __________________________

    def test_test_suites_with_name():
        suite1 = TestSuite(name="Suite 1")
        suite2 = TestSuite(name="Suite 2")
        test_suites = TestSuites(name="Main Suite")
        test_suites.suites.extend([suite1, suite2])
        xml_element = test_suites.get_xml_element()
        assert xml_element.tag == 'testsuites'
        assert xml_element.attrib['name'] == 'Main Suite'
        assert len(xml_element) == 2
        for i, suite in enumerate(test_suites.suites):
>           assert xml_element[i].tag == 'suite'
E           AssertionError: assert 'testsuite' == 'suite'
E             
E             - suite
E             + testsuite

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py:39: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206: PytestCollectionWarning: cannot collect test class 'TestSuites' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py::test_default_test_suites
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py::test_test_suites_with_suites
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_xml_element_0.py::test_test_suites_with_name
======================== 3 failed, 2 warnings in 0.38s =========================
"""