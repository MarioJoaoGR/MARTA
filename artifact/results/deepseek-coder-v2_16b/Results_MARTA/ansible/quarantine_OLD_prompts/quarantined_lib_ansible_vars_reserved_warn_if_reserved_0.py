
import pytest
from unittest.mock import patch
from ansible.vars.reserved import _RESERVED_NAMES
from ansible.utils import display

def warn_if_reserved(myvars, additional=None):
    ''' this function warns if any variable passed conflicts with internally reserved names '''

    if additional is None:
        reserved = _RESERVED_NAMES
    else:
        reserved = _RESERVED_NAMES.union(additional)

    varnames = set(myvars)
    varnames.discard('vars')  # we add this one internally, so safe to ignore
    for varname in varnames.intersection(reserved):
        display.warning('Found variable using reserved name: %s' % varname)

@pytest.mark.parametrize("myvars", [['var1', 'var2', 'vars'], ['var1', 'var2'], []])
def test_warn_if_reserved(myvars):
    with patch('ansible.utils.display.warning') as mock_warning:
        warn_if_reserved(myvars)
        if myvars == ['var1', 'var2', 'vars']:
            assert mock_warning.called, "Expected warning not issued for reserved name 'vars'"
        else:
            assert not mock_warning.called, "Unexpected warning issued for non-reserved names"

@pytest.mark.parametrize("myvars, additional", [([], {'myvar'}), (['var1', 'var2'], {'myvar'})])
def test_warn_if_reserved_custom(myvars, additional):
    with patch('ansible.utils.display.warning') as mock_warning:
        warn_if_reserved(myvars, additional)
        for varname in set(myvars).intersection(additional):
            assert mock_warning.called, f"Expected warning not issued for reserved name '{varname}'"
        if myvars == []:
            assert not mock_warning.called, "Unexpected warning issued for non-reserved names"

@pytest.mark.parametrize("myvars", [[], ['var1', 'var2']])
def test_warn_if_reserved_empty(myvars):
    with patch('ansible.utils.display.warning') as mock_warning:
        warn_if_reserved(myvars)
        assert not mock_warning.called, "Unexpected warning issued for non-reserved names"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 7 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py F [ 14%]
FFFFFF                                                                   [100%]

=================================== FAILURES ===================================
________________________ test_warn_if_reserved[myvars0] ________________________

myvars = ['var1', 'var2', 'vars']

    @pytest.mark.parametrize("myvars", [['var1', 'var2', 'vars'], ['var1', 'var2'], []])
    def test_warn_if_reserved(myvars):
>       with patch('ansible.utils.display.warning') as mock_warning:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fab881e0c40>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'ansible.utils.display' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/display.py'> does not have the attribute 'warning'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
________________________ test_warn_if_reserved[myvars1] ________________________

myvars = ['var1', 'var2']

    @pytest.mark.parametrize("myvars", [['var1', 'var2', 'vars'], ['var1', 'var2'], []])
    def test_warn_if_reserved(myvars):
>       with patch('ansible.utils.display.warning') as mock_warning:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fab87f12e60>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'ansible.utils.display' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/display.py'> does not have the attribute 'warning'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
________________________ test_warn_if_reserved[myvars2] ________________________

myvars = []

    @pytest.mark.parametrize("myvars", [['var1', 'var2', 'vars'], ['var1', 'var2'], []])
    def test_warn_if_reserved(myvars):
>       with patch('ansible.utils.display.warning') as mock_warning:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fab87b97a30>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'ansible.utils.display' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/display.py'> does not have the attribute 'warning'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
______________ test_warn_if_reserved_custom[myvars0-additional0] _______________

myvars = [], additional = {'myvar'}

    @pytest.mark.parametrize("myvars, additional", [([], {'myvar'}), (['var1', 'var2'], {'myvar'})])
    def test_warn_if_reserved_custom(myvars, additional):
>       with patch('ansible.utils.display.warning') as mock_warning:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fab87f702e0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'ansible.utils.display' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/display.py'> does not have the attribute 'warning'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
______________ test_warn_if_reserved_custom[myvars1-additional1] _______________

myvars = ['var1', 'var2'], additional = {'myvar'}

    @pytest.mark.parametrize("myvars, additional", [([], {'myvar'}), (['var1', 'var2'], {'myvar'})])
    def test_warn_if_reserved_custom(myvars, additional):
>       with patch('ansible.utils.display.warning') as mock_warning:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fab888ec6d0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'ansible.utils.display' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/display.py'> does not have the attribute 'warning'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
_____________________ test_warn_if_reserved_empty[myvars0] _____________________

myvars = []

    @pytest.mark.parametrize("myvars", [[], ['var1', 'var2']])
    def test_warn_if_reserved_empty(myvars):
>       with patch('ansible.utils.display.warning') as mock_warning:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fab87b96980>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'ansible.utils.display' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/display.py'> does not have the attribute 'warning'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
_____________________ test_warn_if_reserved_empty[myvars1] _____________________

myvars = ['var1', 'var2']

    @pytest.mark.parametrize("myvars", [[], ['var1', 'var2']])
    def test_warn_if_reserved_empty(myvars):
>       with patch('ansible.utils.display.warning') as mock_warning:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fab87e103d0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'ansible.utils.display' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/display.py'> does not have the attribute 'warning'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py::test_warn_if_reserved[myvars0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py::test_warn_if_reserved[myvars1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py::test_warn_if_reserved[myvars2]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py::test_warn_if_reserved_custom[myvars0-additional0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py::test_warn_if_reserved_custom[myvars1-additional1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py::test_warn_if_reserved_empty[myvars0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py::test_warn_if_reserved_empty[myvars1]
============================== 7 failed in 0.89s ===============================
"""