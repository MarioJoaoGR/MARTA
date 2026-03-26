
import pytest
from sty import rendertype

def test_edge_case():
    # Test initialization with valid edge case values (0 and 255)
    bg_color = rendertype.EightbitBg(0)
    assert bg_color.args == [0]
    
    bg_color = rendertype.EightbitBg(255)
    assert bg_color.args == [255]
    
    # Test initialization with an invalid value, which should raise a ValueError
    with pytest.raises(ValueError):
        rendertype.EightbitBg(256)

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

sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Test initialization with valid edge case values (0 and 255)
        bg_color = rendertype.EightbitBg(0)
        assert bg_color.args == [0]
    
        bg_color = rendertype.EightbitBg(255)
        assert bg_color.args == [255]
    
        # Test initialization with an invalid value, which should raise a ValueError
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_edge_case.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""