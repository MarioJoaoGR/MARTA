
import pytest
from sty.primitive import _render_rules, RenderType, Style

@pytest.fixture
def setup():
    renderfuncs = {RenderType: lambda *args: f"Rendered {args}"}
    rules = [RenderType((1, 2)), Style([RenderType((3, 4))])]
    return _render_rules(renderfuncs, rules)

def test_valid_input(setup):
    rendered_text, flattened_rules = setup
    assert isinstance(rendered_text, str), "Rendered text should be a string"
    assert len(flattened_rules) == 2, "There should be two rules in the flattened list"

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

sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture
    def setup():
        renderfuncs = {RenderType: lambda *args: f"Rendered {args}"}
>       rules = [RenderType((1, 2)), Style([RenderType((3, 4))])]
E       TypeError: RenderType() takes no arguments

sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_valid_input.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.02s ===============================
"""