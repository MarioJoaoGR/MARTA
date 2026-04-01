
import pytest
from isort.format import format_simplified

@pytest.mark.parametrize("input_str, expected", [
    ("from math import sqrt", "math.sqrt"),
    ("import os", "os"),
    ("   from   sys  import path  ", "sys.path"),
    ("", ""),
    ("from math import sqrt\n", "math.sqrt"),
    ("import os\n", "os"),
    ("   from   sys  import path  \n", "sys.path"),
    ("   from   sys  import path  ", "sys.path"),
])
def test_format_simplified(input_str, expected):
    assert format_simplified(input_str) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 8 items

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_input_from.py . [ 12%]
.F...FF                                                                  [100%]

=================================== FAILURES ===================================
________ test_format_simplified[   from   sys  import path  -sys.path0] ________

input_str = '   from   sys  import path  ', expected = 'sys.path'

    @pytest.mark.parametrize("input_str, expected", [
        ("from math import sqrt", "math.sqrt"),
        ("import os", "os"),
        ("   from   sys  import path  ", "sys.path"),
        ("", ""),
        ("from math import sqrt\n", "math.sqrt"),
        ("import os\n", "os"),
        ("   from   sys  import path  \n", "sys.path"),
        ("   from   sys  import path  ", "sys.path"),
    ])
    def test_format_simplified(input_str, expected):
>       assert format_simplified(input_str) == expected
E       AssertionError: assert '  sys .path' == 'sys.path'
E         
E         - sys.path
E         +   sys .path
E         ? ++   +

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_input_from.py:16: AssertionError
_______ test_format_simplified[   from   sys  import path  \n-sys.path] ________

input_str = '   from   sys  import path  \n', expected = 'sys.path'

    @pytest.mark.parametrize("input_str, expected", [
        ("from math import sqrt", "math.sqrt"),
        ("import os", "os"),
        ("   from   sys  import path  ", "sys.path"),
        ("", ""),
        ("from math import sqrt\n", "math.sqrt"),
        ("import os\n", "os"),
        ("   from   sys  import path  \n", "sys.path"),
        ("   from   sys  import path  ", "sys.path"),
    ])
    def test_format_simplified(input_str, expected):
>       assert format_simplified(input_str) == expected
E       AssertionError: assert '  sys .path' == 'sys.path'
E         
E         - sys.path
E         +   sys .path
E         ? ++   +

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_input_from.py:16: AssertionError
________ test_format_simplified[   from   sys  import path  -sys.path1] ________

input_str = '   from   sys  import path  ', expected = 'sys.path'

    @pytest.mark.parametrize("input_str, expected", [
        ("from math import sqrt", "math.sqrt"),
        ("import os", "os"),
        ("   from   sys  import path  ", "sys.path"),
        ("", ""),
        ("from math import sqrt\n", "math.sqrt"),
        ("import os\n", "os"),
        ("   from   sys  import path  \n", "sys.path"),
        ("   from   sys  import path  ", "sys.path"),
    ])
    def test_format_simplified(input_str, expected):
>       assert format_simplified(input_str) == expected
E       AssertionError: assert '  sys .path' == 'sys.path'
E         
E         - sys.path
E         +   sys .path
E         ? ++   +

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_input_from.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_input_from.py::test_format_simplified[   from   sys  import path  -sys.path0]
FAILED isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_input_from.py::test_format_simplified[   from   sys  import path  \n-sys.path]
FAILED isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_input_from.py::test_format_simplified[   from   sys  import path  -sys.path1]
========================= 3 failed, 5 passed in 0.10s ==========================
"""