
import pytest
from lib.ansible.inventory.host import Host

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_host_Host___init___0.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_port_type ____________________________

    def test_invalid_port_type():
        with pytest.raises(TypeError):
>           Host(name='exampleHost', port='invalid_port')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_host_Host___init___0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = exampleHost, name = 'exampleHost', port = 'invalid_port', gen_uuid = True

    def __init__(self, name=None, port=None, gen_uuid=True):
    
        self.vars = {}
        self.groups = []
        self._uuid = None
    
        self.name = name
        self.address = name
    
        if port:
>           self.set_variable('ansible_port', int(port))
E           ValueError: invalid literal for int() with base 10: 'invalid_port'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/inventory/host.py:96: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_host_Host___init___0.py::test_invalid_port_type
============================== 1 failed in 0.43s ===============================
"""