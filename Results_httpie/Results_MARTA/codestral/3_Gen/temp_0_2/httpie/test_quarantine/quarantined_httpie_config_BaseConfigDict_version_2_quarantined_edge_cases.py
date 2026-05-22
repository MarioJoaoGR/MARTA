
import pytest
from unittest.mock import patch
from httpie.config import BaseConfigDict

@pytest.fixture
def base_config():
    return BaseConfigDict(path='/some/file/path')

def test_version_default(base_config):
    with patch('httpie.config.__version__', '1.0.0'):
        assert base_config.version() == '1.0.0'

def test_version_specified(base_config):
    with patch('httpie.config.__meta__', {'httpie': '2.0.0'}), \
         patch('httpie.config.__version__', '1.0.0'):
        assert base_config.version() == '2.0.0'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_version_2_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_version_default _____________________________

base_config = {}

    def test_version_default(base_config):
        with patch('httpie.config.__version__', '1.0.0'):
>           assert base_config.version() == '1.0.0'
E           TypeError: 'str' object is not callable

httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_version_2_test_edge_cases.py:12: TypeError
____________________________ test_version_specified ____________________________

base_config = {}

    def test_version_specified(base_config):
>       with patch('httpie.config.__meta__', {'httpie': '2.0.0'}), \
             patch('httpie.config.__version__', '1.0.0'):

httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_version_2_test_edge_cases.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fdb956a3dd0>

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
E           AttributeError: <module 'httpie.config' from '/projects/F202407648IACDCF2/mario/httpie/httpie/config.py'> does not have the attribute '__meta__'

/usr/local/lib/python3.11/unittest/mock.py:1419: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_version_2_test_edge_cases.py::test_version_default
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_version_2_test_edge_cases.py::test_version_specified
============================== 2 failed in 0.20s ===============================
"""