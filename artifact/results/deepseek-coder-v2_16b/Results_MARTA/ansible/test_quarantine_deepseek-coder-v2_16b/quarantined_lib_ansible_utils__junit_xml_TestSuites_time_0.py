
import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite
import decimal



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_time_without_suites ___________________________

    def test_time_without_suites():
        ts = TestSuites()
>       assert ts.time() == decimal.Decimal('0')
E       TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py:8: TypeError
________________________ test_time_with_different_times ________________________

    def test_time_with_different_times():
        ts = TestSuites()
>       suite1 = TestSuite(name="Suite 1", time=decimal.Decimal('5'))
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'time'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py:12: TypeError
__________________________ test_time_with_same_times ___________________________

    def test_time_with_same_times():
        ts = TestSuites()
>       suite1 = TestSuite(name="Suite 1", time=decimal.Decimal('10'))
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'time'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py:19: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206: PytestCollectionWarning: cannot collect test class 'TestSuites' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_time_0.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_time_0.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py::test_time_without_suites
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py::test_time_with_different_times
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_time_0.py::test_time_with_same_times
======================== 3 failed, 2 warnings in 0.76s =========================
"""