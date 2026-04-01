
import pytest
from sty.register import EfRegister, Style, Sgr

@pytest.fixture
def ef_register():
    return EfRegister()

def test_ef_register_init(ef_register):
    assert hasattr(ef_register, 'b')
    assert isinstance(ef_register.b, Style)
    assert ef_register.b.sgr == Sgr(1)
    assert ef_register.bold.sgr == Sgr(1)
    assert ef_register.dim.sgr == Sgr(2)
    assert ef_register.i.sgr == Sgr(3)
    assert ef_register.italic.sgr == Sgr(3)
    assert ef_register.u.sgr == Sgr(4)
    assert ef_register.underl.sgr == Sgr(4)
    assert ef_register.blink.sgr == Sgr(5)
    assert ef_register.inverse.sgr == Sgr(7)
    assert ef_register.hidden.sgr == Sgr(8)
    assert ef_register.strike.sgr == Sgr(9)
    assert isinstance(ef_register.rs, Style)
    assert ef_register.rs.sgr == (Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29))

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

sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
____________________________ test_ef_register_init _____________________________

ef_register = <sty.register.EfRegister object at 0x106a99480>

    def test_ef_register_init(ef_register):
        assert hasattr(ef_register, 'b')
        assert isinstance(ef_register.b, Style)
>       assert ef_register.b.sgr == Sgr(1)
E       AttributeError: 'Style' object has no attribute 'sgr'

sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:12: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py::test_ef_register_init
============================== 1 failed in 0.02s ===============================
"""