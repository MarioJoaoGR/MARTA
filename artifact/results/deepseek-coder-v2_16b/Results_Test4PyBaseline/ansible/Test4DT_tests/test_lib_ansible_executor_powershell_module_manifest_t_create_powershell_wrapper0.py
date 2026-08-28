# Module: ansible.executor.powershell.module_manifest
import pytest
from ansible.executor.powershell.module_manifest import _create_powershell_wrapper
import base64
import json

# Test cases for _create_powershell_wrapper function

def test_create_powershell_wrapper():
    b_module_data = b'# Some PowerShell code...'
    module_path = 'path/to/module.psm1'
    module_args = {'arg1': 'value1', 'arg2': 'value2'}
    environment = {'VAR1': 'val1', 'VAR2': 'val2'}
    async_timeout = 300
    become = True
    become_method = 'runas'
    become_user = 'username'
    become_password = 'password'
    become_flags = '@("/NOPROFILE")'
    substyle = 'powershell'
    task_vars = {'ansible_version': '2.9'}
    module_fqn = 'Ansible.MyModule'

    wrapper_data = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn)
    
    assert isinstance(wrapper_data, bytes), "Expected wrapper_data to be a byte string"
    # Add more assertions as needed to validate the output format and content

def test_create_powershell_wrapper_no_become():
    b_module_data = b'# Some PowerShell code...'
    module_path = 'path/to/module.psm1'
    module_args = {'arg1': 'value1', 'arg2': 'value2'}
    environment = {'VAR1': 'val1', 'VAR2': 'val2'}
    async_timeout = 300
    become = False
    become_method = None
    become_user = None
    become_password = None
    become_flags = None
    substyle = 'powershell'
    task_vars = {'ansible_version': '2.9'}
    module_fqn = 'Ansible.MyModule'

    wrapper_data = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn)
    
    assert isinstance(wrapper_data, bytes), "Expected wrapper_data to be a byte string"
    # Add more assertions as needed to validate the output format and content without becoming privileges

def test_create_powershell_wrapper_async():
    b_module_data = b'# Some PowerShell code...'
    module_path = 'path/to/module.psm1'
    module_args = {'arg1': 'value1', 'arg2': 'value2'}
    environment = {'VAR1': 'val1', 'VAR2': 'val2'}
    async_timeout = 300
    become = True
    become_method = 'runas'
    become_user = 'username'
    become_password = 'password'
    become_flags = '@("/NOPROFILE")'
    substyle = 'powershell'
    task_vars = {'ansible_version': '2.9'}
    module_fqn = 'Ansible.MyModule'

    wrapper_data = _create_powershell_wrapper(b_module_data, module_path, module_args, environment, async_timeout, become, become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn)
    
    assert isinstance(wrapper_data, bytes), "Expected wrapper_data to be a byte string"
    # Add more assertions as needed to validate the output format and content with asynchronous execution enabled
