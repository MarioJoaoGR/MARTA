
import pytest
from sty import renderfunc

def sgr(num: int) -> str:
    """
    Create a SGR escape sequence.
    """
    return "\033[" + str(num) + "m"

@pytest.mark.parametrize("invalid_input", [None, "string", 3.14, [], {}])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        sgr(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py FFFFF  [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [None, "string", 3.14, [], {}])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py:13: Failed
__________________________ test_invalid_input[string] __________________________

invalid_input = 'string'

    @pytest.mark.parametrize("invalid_input", [None, "string", 3.14, [], {}])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py:13: Failed
___________________________ test_invalid_input[3.14] ___________________________

invalid_input = 3.14

    @pytest.mark.parametrize("invalid_input", [None, "string", 3.14, [], {}])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py:13: Failed
______________________ test_invalid_input[invalid_input3] ______________________

invalid_input = []

    @pytest.mark.parametrize("invalid_input", [None, "string", 3.14, [], {}])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py:13: Failed
______________________ test_invalid_input[invalid_input4] ______________________

invalid_input = {}

    @pytest.mark.parametrize("invalid_input", [None, "string", 3.14, [], {}])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py::test_invalid_input[None]
FAILED sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py::test_invalid_input[string]
FAILED sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py::test_invalid_input[3.14]
FAILED sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py::test_invalid_input[invalid_input3]
FAILED sty/Test4DT_tests/test_sty_renderfunc_sgr_2_test_invalid_input.py::test_invalid_input[invalid_input4]
============================== 5 failed in 0.02s ===============================
"""