
import pytest
from ansible.utils._junit_xml import TestSuite, TestSuites

# Fixture to create a test suite with a given number of disabled tests
@pytest.fixture
def create_test_suite(request):
    num_disabled = request.param
    return TestSuite(name="Test Suite", disabled=num_disabled)

# Scenario: No suites present

# Scenario: All suites are disabled
@pytest.mark.parametrize("create_test_suite", [3], indirect=["create_test_suite"])
def test_disabled_with_all_suites_disabled(create_test_suite):
    test_suites = TestSuites()
    test_suites.suites.append(create_test_suite)
    assert test_suites.disabled() == create_test_suite.disabled

# Scenario: Some suites are disabled
@pytest.mark.parametrize("create_test_suite", [0, 5], indirect=["create_test_suite"])
def test_disabled_with_some_suites_disabled(create_test_suite):
    test_suites = TestSuites()
    test_suites.suites.append(create_test_suite)
    assert test_suites.disabled() == create_test_suite.disabled

# Scenario: A single suite is disabled
@pytest.mark.parametrize("create_test_suite", [7], indirect=["create_test_suite"])
def test_disabled_with_single_suite(create_test_suite):
    test_suites = TestSuites()
    test_suites.suites.append(create_test_suite)
    assert test_suites.disabled() == create_test_suite.disabled
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py F [ 20%]
EEEE                                                                     [100%]

==================================== ERRORS ====================================
_________ ERROR at setup of test_disabled_with_all_suites_disabled[3] __________

request = <SubRequest 'create_test_suite' for <Function test_disabled_with_all_suites_disabled[3]>>

    @pytest.fixture
    def create_test_suite(request):
        num_disabled = request.param
>       return TestSuite(name="Test Suite", disabled=num_disabled)
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'disabled'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py:9: TypeError
_________ ERROR at setup of test_disabled_with_some_suites_disabled[0] _________

request = <SubRequest 'create_test_suite' for <Function test_disabled_with_some_suites_disabled[0]>>

    @pytest.fixture
    def create_test_suite(request):
        num_disabled = request.param
>       return TestSuite(name="Test Suite", disabled=num_disabled)
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'disabled'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py:9: TypeError
_________ ERROR at setup of test_disabled_with_some_suites_disabled[5] _________

request = <SubRequest 'create_test_suite' for <Function test_disabled_with_some_suites_disabled[5]>>

    @pytest.fixture
    def create_test_suite(request):
        num_disabled = request.param
>       return TestSuite(name="Test Suite", disabled=num_disabled)
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'disabled'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py:9: TypeError
_____________ ERROR at setup of test_disabled_with_single_suite[7] _____________

request = <SubRequest 'create_test_suite' for <Function test_disabled_with_single_suite[7]>>

    @pytest.fixture
    def create_test_suite(request):
        num_disabled = request.param
>       return TestSuite(name="Test Suite", disabled=num_disabled)
E       TypeError: TestSuite.__init__() got an unexpected keyword argument 'disabled'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py:9: TypeError
=================================== FAILURES ===================================
_________________________ test_disabled_with_no_suites _________________________

    def test_disabled_with_no_suites():
        test_suites = TestSuites()
>       assert test_suites.disabled() == 0
E       TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py:14: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206: PytestCollectionWarning: cannot collect test class 'TestSuites' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py::test_disabled_with_no_suites
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py::test_disabled_with_all_suites_disabled[3]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py::test_disabled_with_some_suites_disabled[0]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py::test_disabled_with_some_suites_disabled[5]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_disabled_0.py::test_disabled_with_single_suite[7]
=================== 1 failed, 2 warnings, 4 errors in 0.36s ====================
"""