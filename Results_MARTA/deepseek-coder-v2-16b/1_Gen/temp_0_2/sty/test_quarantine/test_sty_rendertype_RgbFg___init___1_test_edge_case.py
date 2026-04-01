
import pytest
from sty import rendertype

def test_edge_case():
    # Define invalid colors with boundary values and null inputs
    invalid_colors = [(-1, 0, 0), (256, 0, 0), (0, -1, 0), (0, 256, 0), (0, 0, -1), (0, 0, 256)]
    
    # Test each invalid color to ensure they raise a ValueError
    for r, g, b in invalid_colors:
        with pytest.raises(ValueError):
            rendertype.RgbFg(r, g, b)

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

sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Define invalid colors with boundary values and null inputs
        invalid_colors = [(-1, 0, 0), (256, 0, 0), (0, -1, 0), (0, 256, 0), (0, 0, -1), (0, 0, 256)]
    
        # Test each invalid color to ensure they raise a ValueError
        for r, g, b in invalid_colors:
>           with pytest.raises(ValueError):
E           Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_edge_case.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""