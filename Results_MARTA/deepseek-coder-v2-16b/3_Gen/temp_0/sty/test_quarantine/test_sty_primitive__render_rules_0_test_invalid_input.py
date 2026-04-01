
import pytest
from sty import primitive
from typing import Callable, Iterable, List, Tuple

class StylingRule:
    pass

class RenderType(StylingRule):
    def __init__(self, args: tuple):
        self.args = args

class Style(StylingRule):
    def __init__(self, rules: List[StylingRule]):
        self.rules = rules

def _render_rules(
    renderfuncs: dict,
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
            raise ValueError("Parameter 'rules' must be of type Iterable[Rule].")

    return rendered, flattened_rules

@pytest.fixture
def setup():
    renderfuncs = {RenderType: lambda *args: f"Rendered {args}"}
    rules = [RenderType((1, 2)), Style([RenderType((3, 4))])]
    return renderfuncs, rules

def test_invalid_input(setup):
    renderfuncs, rules = setup
    with pytest.raises(ValueError):
        _render_rules(renderfuncs, rules)

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

setup = ({<class 'Test4DT_tests.test_sty_primitive__render_rules_0_test_invalid_input.RenderType'>: <function setup.<locals>.<...ct at 0x1034525c0>, <Test4DT_tests.test_sty_primitive__render_rules_0_test_invalid_input.Style object at 0x103452500>])

    def test_invalid_input(setup):
        renderfuncs, rules = setup
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_invalid_input.py:48: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive__render_rules_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""