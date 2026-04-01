
import pytest
from sty.primitive import Register

@pytest.fixture
def custom_register():
    return Register()

def test_as_dict_default_attributes(custom_register):
    # Modify some default attributes to have string values
    custom_register.renderfuncs['test'] = 'test_value'
    custom_register.is_muted = True
    custom_register.eightbit_call = lambda x: str(x)
    custom_register.rgb_call = lambda r, g, b: f"({r}, {g}, {b})"
    
    expected_dict = {
        'renderfuncs': "{'test': 'test_value'}",
        'is_muted': "True",
        'eightbit_call': "(<lambda>)",
        'rgb_call': "(<lambda>)"
    }
    
    assert custom_register.as_dict() == expected_dict

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________ test_as_dict_default_attributes ________________________

custom_register = <sty.primitive.Register object at 0x1026a1960>

    def test_as_dict_default_attributes(custom_register):
        # Modify some default attributes to have string values
        custom_register.renderfuncs['test'] = 'test_value'
        custom_register.is_muted = True
        custom_register.eightbit_call = lambda x: str(x)
        custom_register.rgb_call = lambda r, g, b: f"({r}, {g}, {b})"
    
        expected_dict = {
            'renderfuncs': "{'test': 'test_value'}",
            'is_muted': "True",
            'eightbit_call': "(<lambda>)",
            'rgb_call': "(<lambda>)"
        }
    
>       assert custom_register.as_dict() == expected_dict
E       assert {} == {'eightbit_ca... '(<lambda>)'}
E         
E         Right contains 4 more items:
E         {'eightbit_call': '(<lambda>)',
E          'is_muted': 'True',
E          'renderfuncs': "{'test': 'test_value'}",
E          'rgb_call': '(<lambda>)'}
E         Use -v to get more diff

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_edge_cases.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_edge_cases.py::test_as_dict_default_attributes
============================== 1 failed in 0.02s ===============================
"""