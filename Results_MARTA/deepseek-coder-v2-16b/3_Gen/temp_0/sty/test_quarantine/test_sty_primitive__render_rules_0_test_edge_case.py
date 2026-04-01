
import pytest
from typing import Dict, Callable, List, Tuple, Iterable
from sty.primitive import StylingRule, RenderType, Style

def _render_rules(
    renderfuncs: Dict[type, Callable],
    rules: Iterable[StylingRule],
) -> Tuple[str, Iterable[StylingRule]]:
    rendered: str = ""
    flattened_rules: List[StylingRule] = []

    for rule in rules:
        if isinstance(rule, RenderType):
            f1: Callable = renderfuncs[type(rule)]
            rendered += f1(*rule.args)
            flattened_rules.append(rule)

        elif isinstance(rule, Style):
            r1, r2 = _render_rules(renderfuncs, rule.rules)
            rendered += r1
            flattened_rules.extend(r2)

        else:
            raise ValueError("Parameter 'rules' must be of type Iterable[StylingRule].")

    return rendered, flattened_rules

# Test case for edge case scenario
def test_edge_case():
    renderfuncs = {RenderType: lambda *args: f"Rendered {args}"}
    rules = [RenderType((1, 2)), Style([RenderType((3, 4))])]
    
    rendered_text, flattened_rules = _render_rules(renderfuncs, rules)
    assert rendered_text == "Rendered (1, 2)Rendered (3, 4)"
    assert len(flattened_rules) == 2

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

sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        renderfuncs = {RenderType: lambda *args: f"Rendered {args}"}
>       rules = [RenderType((1, 2)), Style([RenderType((3, 4))])]
E       TypeError: RenderType() takes no arguments

sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_edge_case.py:32: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""