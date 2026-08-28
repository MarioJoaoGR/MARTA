
import pytest
from ansible.plugins.inventory.host_list import InventoryModule
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.utils.addresses import parse_address
from ansible.utils.text import to_native, to_text

@pytest.fixture(scope="module")
def inventory_instance():
    return InventoryModule()

def test_parse_valid_hosts_string(inventory_instance):
    inventory_instance._filename = 'test_inventory.ini'
    host_list = "host1, 192.168.1.1"
    inventory_instance.parse(inventory=None, loader=None, host_list=host_list)
    
    assert 'host1' in inventory_instance.inventory.hosts
    assert '192.168.1.1' in inventory_instance.inventory.hosts

def test_parse_valid_hosts_file(inventory_instance, tmpdir):
    hostfile = tmpdir.join("hosts.ini")
    hostfile.write("[host_list]\nhost1\n192.168.1.1")
    
    inventory_instance._filename = str(hostfile)
    inventory_instance.parse(inventory=None, loader=None, host_list=str(hostfile))
    
    assert 'host1' in inventory_instance.inventory.hosts
    assert '192.168.1.1' in inventory_instance.inventory.hosts

def test_parse_invalid_hosts(inventory_instance):
    inventory_instance._filename = 'test_inventory.ini'
    host_list = "invalid_host, invalid_ip"
    
    with pytest.raises(AnsibleParserError):
        inventory_instance.parse(inventory=None, loader=None, host_list=host_list)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_plugins_inventory_host_list_InventoryModule_parse_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_inventory_host_list_InventoryModule_parse_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_inventory_host_list_InventoryModule_parse_1.py:5: in <module>
    from ansible.utils.addresses import parse_address
E   ModuleNotFoundError: No module named 'ansible.utils.addresses'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_inventory_host_list_InventoryModule_parse_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 1.00s ===============================
"""