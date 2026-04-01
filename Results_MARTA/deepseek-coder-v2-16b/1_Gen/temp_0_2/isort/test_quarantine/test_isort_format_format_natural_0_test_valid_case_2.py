
import pytest
from isort.format import format_natural

def test_valid_case_2():
    assert format_natural("numpy") == "import numpy"
    assert format_natural("math.sin") == "from math import sin"
    assert format_natural("from numpy import array, zeros") == "from numpy import array, zeros"
    assert format_natural("from math import cos, tan") == "from math import cos, tan"
    assert format_natural("numpy.array") == "from numpy import array"
    assert format_natural("numpy.random.rand") == "from numpy.random import rand"
    assert format_natural("math.sqrt(3)") == "from math import sqrt"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_format_format_natural_0_test_valid_case_2.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        assert format_natural("numpy") == "import numpy"
        assert format_natural("math.sin") == "from math import sin"
        assert format_natural("from numpy import array, zeros") == "from numpy import array, zeros"
        assert format_natural("from math import cos, tan") == "from math import cos, tan"
        assert format_natural("numpy.array") == "from numpy import array"
        assert format_natural("numpy.random.rand") == "from numpy.random import rand"
>       assert format_natural("math.sqrt(3)") == "from math import sqrt"
E       AssertionError: assert 'from math import sqrt(3)' == 'from math import sqrt'
E         
E         - from math import sqrt
E         + from math import sqrt(3)
E         ?                      +++

isort/Test4DT_tests/test_isort_format_format_natural_0_test_valid_case_2.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_format_natural_0_test_valid_case_2.py::test_valid_case_2
============================== 1 failed in 0.10s ===============================
"""