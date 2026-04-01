
from sty import Style, RgbFg, Sgr
from typing import Iterable
import pytest

class StylingRule:
    pass

@pytest.mark.parametrize("rules, expected", [
    ((), ""),  # Test with no rules and an empty string value
    ((RgbFg(1, 5, 10), Sgr(1)), "\x1b[38;2;1;5;10m\x1b[1m")  # Test with RgbFg and Sgr rules
])
def test_invalid_input(rules: Iterable[StylingRule], expected: str):
    style = Style(*rules)
    assert isinstance(style, Style)
    assert str(style) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

sty/Test4DT_tests/test_sty_primitive_Style___new___1_test_invalid_input.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________ test_invalid_input[rules1-\x1b[38;2;1;5;10m\x1b[1m] ______________

rules = (<sty.rendertype.RgbFg object at 0x10219fdf0>, <sty.rendertype.Sgr object at 0x10219faf0>)
expected = '\x1b[38;2;1;5;10m\x1b[1m'

    @pytest.mark.parametrize("rules, expected", [
        ((), ""),  # Test with no rules and an empty string value
        ((RgbFg(1, 5, 10), Sgr(1)), "\x1b[38;2;1;5;10m\x1b[1m")  # Test with RgbFg and Sgr rules
    ])
    def test_invalid_input(rules: Iterable[StylingRule], expected: str):
        style = Style(*rules)
        assert isinstance(style, Style)
>       assert str(style) == expected
E       AssertionError: assert '' == '\x1b[38;2;1;5;10m\x1b[1m'
E         
E         - [38;2;1;5;10m[1m

sty/Test4DT_tests/test_sty_primitive_Style___new___1_test_invalid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Style___new___1_test_invalid_input.py::test_invalid_input[rules1-\x1b[38;2;1;5;10m\x1b[1m]
========================= 1 failed, 1 passed in 0.02s ==========================
"""