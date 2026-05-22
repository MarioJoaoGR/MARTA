
import pytest
from unittest.mock import patch

def check_escaped_int(value: str) -> str:
    if not value.startswith('\\'):
        raise ValueError('Not an escaped int')
    try:
        int(value[1:])
    except ValueError as exc:
        raise ValueError('Not an escaped int') from exc
    else:
        return value[1:]

def test_valid_input():
    with patch('__main__.check_escaped_int', return_value='123'):
        result = check_escaped_int('\123')
        assert result == '123'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_3_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       with patch('__main__.check_escaped_int', return_value='123'):

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_3_test_valid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fb57450ae50>

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
E           AttributeError: <module 'pytest.__main__' from '/usr/local/lib/python3.11/site-packages/pytest/__main__.py'> does not have the attribute 'check_escaped_int'

/usr/local/lib/python3.11/unittest/mock.py:1419: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_3_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""