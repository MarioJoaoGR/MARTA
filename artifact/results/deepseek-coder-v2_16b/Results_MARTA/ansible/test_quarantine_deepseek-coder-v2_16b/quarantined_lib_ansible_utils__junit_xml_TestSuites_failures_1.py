
import pytest
from ansible.utils._junit_xml import TestSuite, TestSuites
import decimal

# Test adding suites and calculating failures

# Test converting to pretty XML
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_failures_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________ test_adding_suites_and_calculating_failures __________________

    def test_adding_suites_and_calculating_failures():
>       suite1 = TestSuite(name="Suite 1", disabled=0, errors=3, failures=3, tests=10, time=decimal.Decimal('10'))
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'disabled'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_failures_1.py:8: TypeError
________________________ test_converting_to_pretty_xml _________________________

    def test_converting_to_pretty_xml():
>       suite1 = TestSuite(name="Suite 1", disabled=0, errors=3, failures=3, tests=10, time=decimal.Decimal('10'))
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'disabled'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_failures_1.py:17: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_failures_1.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206: PytestCollectionWarning: cannot collect test class 'TestSuites' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_failures_1.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_failures_1.py::test_adding_suites_and_calculating_failures
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_failures_1.py::test_converting_to_pretty_xml
======================== 2 failed, 2 warnings in 0.75s =========================
"""