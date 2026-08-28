
import pytest
from ansible.utils._junit_xml import TestSuites

@pytest.fixture(scope="module")
def create_test_suites():
    return TestSuites()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_attributes_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_default_attributes ____________________________

create_test_suites = TestSuites(name=None, suites=[])

    def test_default_attributes(create_test_suites):
        attrs = create_test_suites.get_attributes()
>       assert attrs['disabled'] == 'False'
E       AssertionError: assert '0' == 'False'
E         
E         - False
E         + 0

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_attributes_1.py:11: AssertionError
_____________________________ test_set_properties ______________________________

create_test_suites = TestSuites(name=None, suites=[])

    def test_set_properties(create_test_suites):
>       create_test_suites.disabled = False
E       AttributeError: can't set attribute 'disabled'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_attributes_1.py:19: AttributeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206: PytestCollectionWarning: cannot collect test class 'TestSuites' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_get_attributes_1.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_attributes_1.py::test_default_attributes
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_get_attributes_1.py::test_set_properties
========================= 2 failed, 1 warning in 0.73s =========================
"""