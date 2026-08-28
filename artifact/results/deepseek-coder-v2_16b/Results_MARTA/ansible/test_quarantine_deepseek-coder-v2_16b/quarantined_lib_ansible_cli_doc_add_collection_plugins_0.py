
import pytest
from ansible.cli.doc import add_collection_plugins



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        plugin_list = []
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py:7: Failed
__________________ test_add_modules_from_specific_collections __________________

    def test_add_modules_from_specific_collections():
        plugin_list = []
        add_collection_plugins(plugin_list, "module", coll_filter="specific_type")
>       assert len(plugin_list) > 0, "Expected at least one module to be found in specific collections"
E       AssertionError: Expected at least one module to be found in specific collections
E       assert 0 > 0
E        +  where 0 = len([])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py:13: AssertionError
__________________ test_add_modules_from_default_collections ___________________

    def test_add_modules_from_default_collections():
        plugin_list = []
        add_collection_plugins(plugin_list, "module")
>       assert len(plugin_list) > 0, "Expected at least one module to be found in default collections"
E       AssertionError: Expected at least one module to be found in default collections
E       assert 0 > 0
E        +  where 0 = len([])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py::test_invalid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py::test_add_modules_from_specific_collections
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py::test_add_modules_from_default_collections
============================== 3 failed in 0.68s ===============================
"""