
import pytest
from sty import primitive

@pytest.mark.parametrize("test_input, expected", [
    ({"renderfuncs": {}, "is_muted": False, "eightbit_call": lambda x: x, "rgb_call": lambda r, g, b: (r, g, b)}, {})
])
def test_sty_primitive_Register___init___(test_input, expected):
    register = primitive.Register()
    assert register.renderfuncs == expected["renderfuncs"]
    assert register.is_muted == expected["is_muted"]
    assert register.eightbit_call(1) == expected["eightbit_call"](1)
    assert register.rgb_call(255, 0, 0) == expected["rgb_call"](255, 0, 0)

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

sty/Test4DT_tests/test_sty_primitive_Register___init___1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_________ test_sty_primitive_Register___init___[test_input0-expected0] _________

test_input = {'eightbit_call': <function <lambda> at 0x101bca560>, 'is_muted': False, 'renderfuncs': {}, 'rgb_call': <function <lambda> at 0x101bcab00>}
expected = {}

    @pytest.mark.parametrize("test_input, expected", [
        ({"renderfuncs": {}, "is_muted": False, "eightbit_call": lambda x: x, "rgb_call": lambda r, g, b: (r, g, b)}, {})
    ])
    def test_sty_primitive_Register___init___(test_input, expected):
        register = primitive.Register()
>       assert register.renderfuncs == expected["renderfuncs"]
E       KeyError: 'renderfuncs'

sty/Test4DT_tests/test_sty_primitive_Register___init___1_test_edge_case.py:10: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___init___1_test_edge_case.py::test_sty_primitive_Register___init___[test_input0-expected0]
============================== 1 failed in 0.02s ===============================

"""