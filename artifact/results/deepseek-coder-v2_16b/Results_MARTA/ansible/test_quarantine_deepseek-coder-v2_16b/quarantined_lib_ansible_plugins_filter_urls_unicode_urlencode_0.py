
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_path_component ________________________

    def test_valid_input_path_component():
        # Test encoding for path component of a URL with valid input
        result = unicode_urlencode("Hello World!")
>       assert result == "Hello%20World!"
E       AssertionError: assert 'Hello%20World%21' == 'Hello%20World!'
E         
E         - Hello%20World!
E         ?              ^
E         + Hello%20World%21
E         ?              ^^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_0.py:8: AssertionError
________________________ test_valid_input_query_string _________________________

    def test_valid_input_query_string():
        # Test encoding for query string in a URL with valid input
        result = unicode_urlencode("Hello+World!", for_qs=True)
>       assert result == "Hello%2BWorld!"
E       AssertionError: assert 'Hello%2BWorld%21' == 'Hello%2BWorld!'
E         
E         - Hello%2BWorld!
E         ?              ^
E         + Hello%2BWorld%21
E         ?              ^^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_0.py::test_valid_input_path_component
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_urls_unicode_urlencode_0.py::test_valid_input_query_string
============================== 2 failed in 0.44s ===============================
"""