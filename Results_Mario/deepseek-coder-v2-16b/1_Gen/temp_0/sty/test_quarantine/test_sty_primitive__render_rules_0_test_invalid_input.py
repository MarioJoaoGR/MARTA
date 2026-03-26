
import pytest
from typing import Dict, Callable, List, Tuple, Iterable
from sty.primitive import _render_rules, RenderType, Style, StylingRule, Renderfuncs

def test_invalid_input():
    renderfuncs = {RenderType: lambda *args: f"Rendered {args}"}
    rules = [RenderType((1, 2)), Style([RenderType((3, 4))])]
    
    with pytest.raises(ValueError):
        _render_rules(renderfuncs, "not an iterable")

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

sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        renderfuncs = {RenderType: lambda *args: f"Rendered {args}"}
>       rules = [RenderType((1, 2)), Style([RenderType((3, 4))])]
E       TypeError: RenderType() takes no arguments

sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_invalid_input.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================

"""