
import pytest
from ansible.utils.context_objects import CLIArgs

def _make_immutable(value):
    if isinstance(value, dict):
        return ImmutableDict(value)
    elif isinstance(value, (list, tuple)):
        return ImmutableList(value)
    else:
        return value

class ImmutableDict(dict):
    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)
        super().__setattr__('_dict', self._dict)
    
    def __getattribute__(self, name):
        if name == '_dict':
            return object.__getattribute__(self, name)
        return self._dict.get(name)
    
    def __setattr__(self, key, value):
        raise TypeError("ImmutableDict is immutable")
    
    def __delattr__(self, key):
        raise TypeError("ImmutableDict is immutable")

class ImmutableList(tuple):
    def __init__(self, *args, **kwargs):
        self._tuple = tuple(*args, **kwargs)
        super().__setattr__('_tuple', self._tuple)
    
    def __getattribute__(self, name):
        if name == '_tuple':
            return object.__getattribute__(self, name)
        return self._tuple.get(name)
    
    def __setattr__(self, key, value):
        raise TypeError("ImmutableList is immutable")
    
    def __delattr__(self, key):
        raise TypeError("ImmutableList is immutable")

class TestCLIArgs:
    @pytest.fixture
    def cli_args(self):
        return CLIArgs({'arg1': [1, 2, 3], 'arg2': {'a': 'b'}})

    def test_cli_args_initialization(self, cli_args):
        assert isinstance(cli_args, CLIArgs)
        assert cli_args['arg1'] == (1, 2, 3)
        assert isinstance(cli_args['arg2'], ImmutableDict)
        assert cli_args['arg2']['a'] == 'b'

    def test_immutable_dict(self):
        immutable_dict = ImmutableDict({'a': 'b'})
        with pytest.raises(TypeError):
            immutable_dict['a'] = 'c'
        with pytest.raises(TypeError):
            del immutable_dict['a']

    def test_immutable_list(self):
        immutable_list = ImmutableList([1, 2, 3])
        with pytest.raises(TypeError):
            immutable_list[0] = 4
        with pytest.raises(TypeError):
            del immutable_list[0]
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________ TestCLIArgs.test_cli_args_initialization ___________________

self = <test_lib_ansible_utils_context_objects_CLIArgs___init___0.TestCLIArgs object at 0x7f85b7419780>
cli_args = ImmutableDict({'arg1': (1, 2, 3), 'arg2': ImmutableDict({'a': 'b'})})

    def test_cli_args_initialization(self, cli_args):
        assert isinstance(cli_args, CLIArgs)
        assert cli_args['arg1'] == (1, 2, 3)
>       assert isinstance(cli_args['arg2'], ImmutableDict)
E       AssertionError: assert False
E        +  where False = isinstance(ImmutableDict({'a': 'b'}), ImmutableDict)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py:53: AssertionError
_______________________ TestCLIArgs.test_immutable_dict ________________________

self = <test_lib_ansible_utils_context_objects_CLIArgs___init___0.TestCLIArgs object at 0x7f85b7419900>

    def test_immutable_dict(self):
>       immutable_dict = ImmutableDict({'a': 'b'})

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py:57: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py:15: in __init__
    self._dict = dict(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = {}, key = '_dict', value = {'a': 'b'}

    def __setattr__(self, key, value):
>       raise TypeError("ImmutableDict is immutable")
E       TypeError: ImmutableDict is immutable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py:24: TypeError
_______________________ TestCLIArgs.test_immutable_list ________________________

self = <test_lib_ansible_utils_context_objects_CLIArgs___init___0.TestCLIArgs object at 0x7f85b7419870>

    def test_immutable_list(self):
>       immutable_list = ImmutableList([1, 2, 3])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py:64: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py:31: in __init__
    self._tuple = tuple(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = (1, 2, 3), key = '_tuple', value = (1, 2, 3)

    def __setattr__(self, key, value):
>       raise TypeError("ImmutableList is immutable")
E       TypeError: ImmutableList is immutable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py:40: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py::TestCLIArgs::test_cli_args_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py::TestCLIArgs::test_immutable_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects_CLIArgs___init___0.py::TestCLIArgs::test_immutable_list
============================== 3 failed in 0.37s ===============================
"""