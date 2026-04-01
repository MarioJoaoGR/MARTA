
import pytest
from sty.primitive import Register

@pytest.fixture
def register():
    return Register()

def test_as_dict(register):
    # Test that as_dict method returns a dictionary with correct keys and values
    assert isinstance(register.as_dict(), dict)
    expected_keys = {'renderfuncs', 'is_muted', 'eightbit_call', 'rgb_call'}
    actual_keys = set(register.as_dict().keys())
    assert expected_keys == actual_keys

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

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_as_dict _________________________________

register = <sty.primitive.Register object at 0x1025d5480>

    def test_as_dict(register):
        # Test that as_dict method returns a dictionary with correct keys and values
        assert isinstance(register.as_dict(), dict)
        expected_keys = {'renderfuncs', 'is_muted', 'eightbit_call', 'rgb_call'}
        actual_keys = set(register.as_dict().keys())
>       assert expected_keys == actual_keys
E       AssertionError: assert {'eightbit_ca...', 'rgb_call'} == set()
E         
E         Extra items in the left set:
E         'renderfuncs'
E         'is_muted'
E         'rgb_call'
E         'eightbit_call'
E         Use -v to get more diff

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_edge_case.py::test_as_dict
============================== 1 failed in 0.02s ===============================

"""