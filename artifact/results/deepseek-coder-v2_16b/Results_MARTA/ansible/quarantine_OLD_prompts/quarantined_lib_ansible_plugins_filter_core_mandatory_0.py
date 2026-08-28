
import pytest
from ansible.errors import AnsibleFilterError
from jinja2.runtime import Undefined
from unittest.mock import patch
from ansible.plugins.filter.core import to_text, to_native



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_mandatory_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_mandatory_with_undefined _________________________

    def test_mandatory_with_undefined():
        with pytest.raises(AnsibleFilterError) as excinfo:
>           mandatory(Undefined())
E           NameError: name 'mandatory' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_mandatory_0.py:10: NameError
_________________________ test_mandatory_with_defined __________________________

    def test_mandatory_with_defined():
        with patch('ansible.plugins.filter.core.to_text', return_value='test'):
>           result = mandatory("test")
E           NameError: name 'mandatory' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_mandatory_0.py:15: NameError
______________________ test_mandatory_with_custom_message ______________________

    def test_mandatory_with_custom_message():
        with pytest.raises(AnsibleFilterError) as excinfo:
>           mandatory(Undefined(), msg="Custom error message: 'undefined_var' must be defined.")
E           NameError: name 'mandatory' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_mandatory_0.py:20: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_mandatory_0.py::test_mandatory_with_undefined
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_mandatory_0.py::test_mandatory_with_defined
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_mandatory_0.py::test_mandatory_with_custom_message
============================== 3 failed in 0.52s ===============================
"""