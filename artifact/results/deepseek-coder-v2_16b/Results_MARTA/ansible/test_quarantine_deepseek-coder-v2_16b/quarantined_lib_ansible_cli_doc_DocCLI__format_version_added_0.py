
import pytest
from ansible.cli.doc import DocCLI



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________ test_format_version_added_with_collection ___________________

    def test_format_version_added_with_collection():
        version_added = '3.0'
        version_added_collection = 'ansible.builtin'
        result = DocCLI._format_version_added(version_added, version_added_collection)
>       assert result == '3.0 of ansible-core', f"Expected '3.0 of ansible-core' but got {result}"
E       AssertionError: Expected '3.0 of ansible-core' but got version 3.0 of ansible-core
E       assert 'version 3.0 of ansible-core' == '3.0 of ansible-core'
E         
E         - 3.0 of ansible-core
E         + version 3.0 of ansible-core
E         ? ++++++++

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_0.py:9: AssertionError
_____________________ test_format_version_added_historical _____________________

    def test_format_version_added_historical():
        version_added = 'historical'
        result = DocCLI._format_version_added(version_added)
>       assert result == 'historical', f"Expected 'historical' but got {result}"
E       AssertionError: Expected 'historical' but got version historical
E       assert 'version historical' == 'historical'
E         
E         - historical
E         + version historical

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_0.py:14: AssertionError
________________________ test_format_version_added_none ________________________

    def test_format_version_added_none():
        version_added = None
        result = DocCLI._format_version_added(version_added)
>       assert result == '', "Expected empty string for None version_added"
E       AssertionError: Expected empty string for None version_added
E       assert 'version None' == ''
E         
E         + version None

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_0.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_0.py::test_format_version_added_with_collection
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_0.py::test_format_version_added_historical
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_0.py::test_format_version_added_none
============================== 3 failed in 0.63s ===============================
"""