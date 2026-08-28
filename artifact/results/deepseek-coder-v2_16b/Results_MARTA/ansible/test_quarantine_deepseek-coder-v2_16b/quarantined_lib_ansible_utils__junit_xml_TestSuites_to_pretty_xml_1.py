
import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
__________________________ test_to_pretty_xml_default __________________________

    def test_to_pretty_xml_default():
        test_suites = TestSuites()
        xml_string = test_suites.to_pretty_xml()
        assert '<testsuites' in xml_string
>       assert 'disabled="False"' in xml_string
E       assert 'disabled="False"' in '<?xml version="1.0" ?>\n<testsuites disabled="0" errors="0" failures="0" tests="0" time="0"/>\n'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py:9: AssertionError
_____________________ test_to_pretty_xml_with_named_suite ______________________

    def test_to_pretty_xml_with_named_suite():
        suite1 = TestSuite(name="Example Suite")
        test_suites = TestSuites()
        test_suites.suites.append(suite1)
        xml_string = test_suites.to_pretty_xml()
        assert '<testsuites' in xml_string
>       assert 'disabled="False"' in xml_string
E       assert 'disabled="False"' in '<?xml version="1.0" ?>\n<testsuites disabled="0" errors="0" failures="0" tests="0" time="0">\n\t<testsuite disabled="0" errors="0" failures="0" name="Example Suite" skipped="0" tests="0" time="0"/>\n</testsuites>\n'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py:22: AssertionError
___________________ test_to_pretty_xml_with_multiple_suites ____________________

    def test_to_pretty_xml_with_multiple_suites():
        suite1 = TestSuite(name="Suite 1")
        suite2 = TestSuite(name="Suite 2")
        test_suites = TestSuites()
        test_suites.suites.extend([suite1, suite2])
        xml_string = test_suites.to_pretty_xml()
        assert '<testsuites' in xml_string
>       assert 'disabled="False"' in xml_string
E       assert 'disabled="False"' in '<?xml version="1.0" ?>\n<testsuites disabled="0" errors="0" failures="0" tests="0" time="0">\n\t<testsuite disabled=".../>\n\t<testsuite disabled="0" errors="0" failures="0" name="Suite 2" skipped="0" tests="0" time="0"/>\n</testsuites>\n'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py:38: AssertionError
______________________ test_to_pretty_xml_with_properties ______________________

    def test_to_pretty_xml_with_properties():
        suite1 = TestSuite(name="Suite 1", properties={"env": "test"})
        test_suites = TestSuites()
        test_suites.suites.append(suite1)
        xml_string = test_suites.to_pretty_xml()
        assert '<testsuites' in xml_string
>       assert 'disabled="False"' in xml_string
E       assert 'disabled="False"' in '<?xml version="1.0" ?>\n<testsuites disabled="0" errors="0" failures="0" tests="0" time="0">\n\t<testsuite disabled="...="0">\n\t\t<properties>\n\t\t\t<property name="env" value="test"/>\n\t\t</properties>\n\t</testsuite>\n</testsuites>\n'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py:54: AssertionError
________________________ test_to_pretty_xml_with_errors ________________________

    def test_to_pretty_xml_with_errors():
>       suite1 = TestSuite(name="Suite 1", errors=1)
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'errors'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py:65: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206: PytestCollectionWarning: cannot collect test class 'TestSuites' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py::test_to_pretty_xml_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py::test_to_pretty_xml_with_named_suite
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py::test_to_pretty_xml_with_multiple_suites
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py::test_to_pretty_xml_with_properties
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_1.py::test_to_pretty_xml_with_errors
======================== 5 failed, 2 warnings in 0.76s =========================
"""