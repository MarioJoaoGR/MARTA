
import pytest
from httpie.cli.dicts import MultiValueOrderedDict

def test_valid_inputs():
    mvod = MultiValueOrderedDict()
    
    # Add some valid inputs to the dictionary
    mvod['key1'] = 'value1'
    mvod['key2'] = ['value2', 'value3']
    
    assert isinstance(mvod['key2'], list)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_MultiValueOrderedDict_items_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        mvod = MultiValueOrderedDict()
    
        # Add some valid inputs to the dictionary
        mvod['key1'] = 'value1'
>       mvod['key2'] = ['value2', 'value3']

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_MultiValueOrderedDict_items_0_test_valid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = MultiValueOrderedDict([('key1', 'value1')]), key = 'key2'
value = ['value2', 'value3']

    def __setitem__(self, key, value):
        """
        If `key` is assigned more than once, `self[key]` holds a
        `list` of all the values.
    
        This allows having multiple fields with the same name in form
        data and URL params.
    
        """
>       assert not isinstance(value, list)
E       AssertionError

httpie/httpie/cli/dicts.py:65: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_MultiValueOrderedDict_items_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.13s ===============================
"""