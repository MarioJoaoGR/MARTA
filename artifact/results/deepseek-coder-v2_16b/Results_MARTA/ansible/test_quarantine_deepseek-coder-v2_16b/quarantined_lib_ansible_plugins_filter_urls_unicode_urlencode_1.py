
import pytest
from ansible.plugins.filter.urls import unicode_urlencode


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_path_component ________________________

    def test_valid_input_path_component():
        string = "Hello World!"
        encoded_string = unicode_urlencode(string)
>       assert encoded_string == 'Hello%20World!', f"Expected 'Hello%20World!' but got {encoded_string}"
E       AssertionError: Expected 'Hello%20World!' but got Hello%20World%21
E       assert 'Hello%20World%21' == 'Hello%20World!'
E         
E         - Hello%20World!
E         ?              ^
E         + Hello%20World%21
E         ?              ^^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_1.py:8: AssertionError
________________________ test_valid_input_query_string _________________________

    def test_valid_input_query_string():
        string = "Hello+World!"
        encoded_string = unicode_urlencode(string, for_qs=True)
>       assert encoded_string == 'Hello%2BWorld!', f"Expected 'Hello%2BWorld!' but got {encoded_string}"
E       AssertionError: Expected 'Hello%2BWorld!' but got Hello%2BWorld%21
E       assert 'Hello%2BWorld%21' == 'Hello%2BWorld!'
E         
E         - Hello%2BWorld!
E         ?              ^
E         + Hello%2BWorld%21
E         ?              ^^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_1.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_1.py::test_valid_input_path_component
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_1.py::test_valid_input_query_string
============================== 2 failed in 0.74s ===============================
"""