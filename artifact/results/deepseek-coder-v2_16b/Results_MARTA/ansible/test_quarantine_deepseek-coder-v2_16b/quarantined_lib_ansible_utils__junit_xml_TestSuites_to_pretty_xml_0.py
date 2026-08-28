
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_inputs_happy_path _________________________

    def test_valid_inputs_happy_path():
        valid_test_suites = TestSuites()
        xml_string = valid_test_suites.to_pretty_xml()
        assert isinstance(xml_string, str), "Expected XML string but got something else"
        assert "<testsuites" in xml_string, "XML should start with <testsuites>"
        assert "disabled=" in xml_string, "XML should have a disabled attribute"
        assert "errors=" in xml_string, "XML should have an errors attribute"
        assert "failures=" in xml_string, "XML should have a failures attribute"
>       assert "name=" in xml_string, "XML should have a name attribute"
E       AssertionError: XML should have a name attribute
E       assert 'name=' in '<?xml version="1.0" ?>\n<testsuites disabled="0" errors="0" failures="0" tests="0" time="0"/>\n'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_0.py:13: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_0.py:16: Failed
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:206: PytestCollectionWarning: cannot collect test class 'TestSuites' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_0.py)
    @dataclasses.dataclass

../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/_junit_xml.py:128: PytestCollectionWarning: cannot collect test class 'TestSuite' because it has a __init__ constructor (from: test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_0.py)
    @dataclasses.dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_0.py::test_valid_inputs_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils__junit_xml_TestSuites_to_pretty_xml_0.py::test_edge_cases
======================== 2 failed, 2 warnings in 0.37s =========================
"""