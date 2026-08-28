
import pytest
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector
import selinux

# Test case for collecting SELinux facts when the library is missing
def test_collect_with_missing_library():
    class MockSelinux:
        @staticmethod
        def is_selinux_enabled():
            return False
    
    selinux.is_selinux_enabled = MockSelinux.is_selinux_enabled
    
    collector = SelinuxFactCollector()
    facts = collector.collect()
    
    assert 'status' in facts['selinux']
    assert facts['selinux']['status'] == 'Missing selinux Python library'
    assert 'selinux_python_present' in facts
    assert not facts['selinux_python_present']

# Test case for collecting SELinux facts when the library is present and enabled
def test_collect_with_enabled_selinux():
    class MockSelinux:
        @staticmethod
        def is_selinux_enabled():
            return True
        
        @staticmethod
        def security_policyvers():
            return 308
        
        @staticmethod
        def selinux_getenforcemode():
            return (0, 'enforcing')
        
        @staticmethod
        def security_getenforce():
            return 'enforcing'
        
        @staticmethod
        def selinux_getpolicytype():
            return (0, 'targeted')
    
    selinux.is_selinux_enabled = MockSelinux.is_selinux_enabled
    selinux.security_policyvers = MockSelinux.security_policyvers
    selinux.selinux_getenforcemode = MockSelinux.selinux_getenforcemode
    selinux.security_getenforce = MockSelinux.security_getenforce
    selinux.selinux_getpolicytype = MockSelinux.selinux_getpolicytype
    
    collector = SelinuxFactCollector()
    facts = collector.collect()
    
    assert 'status' in facts['selinux']
    assert facts['selinux']['status'] == 'enabled'
    assert 'policyvers' in facts['selinux']
    assert facts['selinux']['policyvers'] == 308
    assert 'config_mode' in facts['selinux']
    assert facts['selinux']['config_mode'] == 'enforcing'
    assert 'mode' in facts['selinux']
    assert facts['selinux']['mode'] == 'enforcing'
    assert 'type' in facts['selinux']
    assert facts['selinux']['type'] == 'targeted'
    assert 'selinux_python_present' in facts
    assert facts['selinux_python_present']

# Test case for collecting SELinux facts when the library is present but disabled
def test_collect_with_disabled_selinux():
    class MockSelinux:
        @staticmethod
        def is_selinux_enabled():
            return False
    
    selinux.is_selinux_enabled = MockSelinux.is_selinux_enabled
    
    collector = SelinuxFactCollector()
    facts = collector.collect()
    
    assert 'status' in facts['selinux']
    assert facts['selinux']['status'] == 'disabled'
    assert 'policyvers' not in facts['selinux']
    assert 'config_mode' not in facts['selinux']
    assert 'mode' not in facts['selinux']
    assert 'type' not in facts['selinux']
    assert 'selinux_python_present' in facts
    assert facts['selinux_python_present']

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
_ ERROR collecting test_lib_ansible_module_utils_facts_system_selinux_SelinuxFactCollector_collect_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_selinux_SelinuxFactCollector_collect_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_selinux_SelinuxFactCollector_collect_0.py:4: in <module>
    import selinux
E   ModuleNotFoundError: No module named 'selinux'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_selinux_SelinuxFactCollector_collect_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.43s ===============================
"""