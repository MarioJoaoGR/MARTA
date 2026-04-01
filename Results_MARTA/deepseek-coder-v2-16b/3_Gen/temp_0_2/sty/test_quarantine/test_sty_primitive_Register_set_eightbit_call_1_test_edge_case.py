
import pytest
from sty import primitive

class Register:
    def __init__(self):
        self.renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def set_eightbit_call(self, rendertype):
        func = self.renderfuncs[rendertype]
        self.eightbit_call = func

def test_edge_case():
    reg = Register()
    with pytest.raises(TypeError):
        reg.set_eightbit_call(None)

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

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        reg = Register()
        with pytest.raises(TypeError):
>           reg.set_eightbit_call(None)

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_1_test_edge_case.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_sty_primitive_Register_set_eightbit_call_1_test_edge_case.Register object at 0x10408c730>
rendertype = None

    def set_eightbit_call(self, rendertype):
>       func = self.renderfuncs[rendertype]
E       KeyError: None

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_1_test_edge_case.py:13: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""