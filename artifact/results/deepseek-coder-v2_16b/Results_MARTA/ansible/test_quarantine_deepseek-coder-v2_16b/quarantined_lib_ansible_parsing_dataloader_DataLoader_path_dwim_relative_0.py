
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_path_dwim_relative_0.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_load_from_file __________________________

    def test_invalid_load_from_file():
        dataloader = DataLoader()
        with pytest.raises(AnsibleFileNotFound) as excinfo:
            dataloader.load_from_file('nonexistentfile.yaml')
>       assert str(excinfo.value) == "Unable to retrieve file contents"
E       AssertionError: assert 'Unable to re...te_src option' == 'Unable to re...file contents'
E         
E         - Unable to retrieve file contents
E         + Unable to retrieve file contents
E         ?                                 +
E         + Could not find or access '/data/results/harness/sandbox/marta/nonexistentfile.yaml' on the Ansible Controller.
E         + If you are using a module and expect the file to exist on the remote, see the remote_src option

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_path_dwim_relative_0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_path_dwim_relative_0.py::test_invalid_load_from_file
============================== 1 failed in 0.26s ===============================
"""