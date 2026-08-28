
import pytest
from ansible.utils._junit_xml import TestSuite, TestCase
import datetime






"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 6 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
_____________________________ test_add_test_cases ______________________________

    def test_add_test_cases():
        suite = TestSuite(name="Example Suite")
>       case1 = TestCase(name="Test Case 1", is_error=True)
E       TypeError: TestCase.__init__() got an unexpected keyword argument 'is_error'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py:8: TypeError
______________________________ test_count_errors _______________________________

    def test_count_errors():
        suite = TestSuite(name="Example Suite")
>       case1 = TestCase(name="Test Case 1", is_error=True)
E       TypeError: TestCase.__init__() got an unexpected keyword argument 'is_error'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py:16: TypeError
_____________________________ test_count_failures ______________________________

    def test_count_failures():
        suite = TestSuite(name="Example Suite")
>       case1 = TestCase(name="Test Case 1", is_error=False)
E       TypeError: TestCase.__init__() got an unexpected keyword argument 'is_error'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py:24: TypeError
_____________________________ test_count_disabled ______________________________

    def test_count_disabled():
        suite = TestSuite(name="Example Suite")
        with pytest.raises(NotImplementedError):
>           suite.disabled()
E           TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py:33: TypeError
______________________________ test_count_skipped ______________________________

    def test_count_skipped():
        suite = TestSuite(name="Example Suite")
        with pytest.raises(NotImplementedError):
>           suite.skipped()
E           TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py:38: TypeError
__________________________ test_total_tests_and_time ___________________________

    def test_total_tests_and_time():
        suite = TestSuite(name="Example Suite")
        with pytest.raises(NotImplementedError):
>           suite.tests()
E           TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py:43: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:67
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:67: PytestCollectionWarning: cannot collect test class 'TestCase' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py::test_add_test_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py::test_count_errors
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py::test_count_failures
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py::test_count_disabled
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py::test_count_skipped
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_0.py::test_total_tests_and_time
======================== 6 failed, 2 warnings in 0.38s =========================
"""