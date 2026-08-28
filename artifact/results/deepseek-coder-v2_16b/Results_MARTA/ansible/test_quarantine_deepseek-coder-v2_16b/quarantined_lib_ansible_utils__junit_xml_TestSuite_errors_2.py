
import pytest
from ansible.utils._junit_xml import TestSuite, TestCase


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_adding_test_cases ____________________________

    def test_adding_test_cases():
        suite = TestSuite(name="Example Suite")
>       case1 = TestCase(name="Test Case 1", is_error=True)
E       TypeError: TestCase.__init__() got an unexpected keyword argument 'is_error'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_2.py:7: TypeError
______________________________ test_errors_method ______________________________

    def test_errors_method():
        suite = TestSuite(name="Example Suite")
>       case1 = TestCase(name="Test Case 1", is_error=True)
E       TypeError: TestCase.__init__() got an unexpected keyword argument 'is_error'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_2.py:14: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuite_errors_2.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:67
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:67: PytestCollectionWarning: cannot collect test class 'TestCase' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuite_errors_2.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_2.py::test_adding_test_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuite_errors_2.py::test_errors_method
======================== 2 failed, 2 warnings in 0.72s =========================
"""