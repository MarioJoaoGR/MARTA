
# Module: sty.rendertype
# test_sty_rendertype.py
from sty.rendertype import EightbitBg

def test_eightbitbg_valid_input():
    # Test initialization with a valid 8-bit color number
    bg_color = EightbitBg(123)
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

sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0.py F         [100%]

=================================== FAILURES ===================================
_________________________ test_eightbitbg_valid_input __________________________

    def test_eightbitbg_valid_input():
        # Test initialization with a valid 8-bit color number
        bg_color = EightbitBg(123)
>       assert hasattr(bg_color, 'num'), f"Expected attribute 'num' to be present on object {bg_color}"
E       AssertionError: Expected attribute 'num' to be present on object <sty.rendertype.EightbitBg object at 0x103d05d80>
E       assert False
E        +  where False = hasattr(<sty.rendertype.EightbitBg object at 0x103d05d80>, 'num')

sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0.py::test_eightbitbg_valid_input
============================== 1 failed in 0.01s ===============================

"""