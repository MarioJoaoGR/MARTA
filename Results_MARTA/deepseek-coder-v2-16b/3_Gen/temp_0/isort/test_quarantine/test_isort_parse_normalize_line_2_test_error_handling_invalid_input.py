
import pytest
from isort.parse import normalize_line  # Assuming this module exists and contains the necessary functions

@pytest.mark.parametrize("raw_line, expected_normalized, expected_raw", [
    ("from .cimport numpy", "from  cimport numpy", "from .cimport numpy"),
    ("from .. import math", "from  import math", "from .. import math"),
    ("\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt")
])
def test_normalize_line(raw_line, expected_normalized, expected_raw):
    with pytest.raises(TypeError) as excinfo:
        normalize_line(12345)  # Test invalid input type
    assert str(excinfo.value) == "Expected a string, but got <class 'int'>"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_parse_normalize_line_2_test_error_handling_invalid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_ test_normalize_line[from .cimport numpy-from  cimport numpy-from .cimport numpy] _

raw_line = 'from .cimport numpy', expected_normalized = 'from  cimport numpy'
expected_raw = 'from .cimport numpy'

    @pytest.mark.parametrize("raw_line, expected_normalized, expected_raw", [
        ("from .cimport numpy", "from  cimport numpy", "from .cimport numpy"),
        ("from .. import math", "from  import math", "from .. import math"),
        ("\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt")
    ])
    def test_normalize_line(raw_line, expected_normalized, expected_raw):
        with pytest.raises(TypeError) as excinfo:
            normalize_line(12345)  # Test invalid input type
>       assert str(excinfo.value) == "Expected a string, but got <class 'int'>"
E       assert "expected str...ct, got 'int'" == "Expected a s...<class 'int'>"
E         
E         - Expected a string, but got <class 'int'>
E         + expected string or bytes-like object, got 'int'

isort/Test4DT_tests/test_isort_parse_normalize_line_2_test_error_handling_invalid_input.py:13: AssertionError
_ test_normalize_line[from .. import math-from  import math-from .. import math] _

raw_line = 'from .. import math', expected_normalized = 'from  import math'
expected_raw = 'from .. import math'

    @pytest.mark.parametrize("raw_line, expected_normalized, expected_raw", [
        ("from .cimport numpy", "from  cimport numpy", "from .cimport numpy"),
        ("from .. import math", "from  import math", "from .. import math"),
        ("\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt")
    ])
    def test_normalize_line(raw_line, expected_normalized, expected_raw):
        with pytest.raises(TypeError) as excinfo:
            normalize_line(12345)  # Test invalid input type
>       assert str(excinfo.value) == "Expected a string, but got <class 'int'>"
E       assert "expected str...ct, got 'int'" == "Expected a s...<class 'int'>"
E         
E         - Expected a string, but got <class 'int'>
E         + expected string or bytes-like object, got 'int'

isort/Test4DT_tests/test_isort_parse_normalize_line_2_test_error_handling_invalid_input.py:13: AssertionError
_ test_normalize_line[\tfrom   numpy import sqrt-\tfrom   numpy import sqrt-\tfrom   numpy import sqrt] _

raw_line = '\tfrom   numpy import sqrt'
expected_normalized = '\tfrom   numpy import sqrt'
expected_raw = '\tfrom   numpy import sqrt'

    @pytest.mark.parametrize("raw_line, expected_normalized, expected_raw", [
        ("from .cimport numpy", "from  cimport numpy", "from .cimport numpy"),
        ("from .. import math", "from  import math", "from .. import math"),
        ("\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt", "\tfrom   numpy import sqrt")
    ])
    def test_normalize_line(raw_line, expected_normalized, expected_raw):
        with pytest.raises(TypeError) as excinfo:
            normalize_line(12345)  # Test invalid input type
>       assert str(excinfo.value) == "Expected a string, but got <class 'int'>"
E       assert "expected str...ct, got 'int'" == "Expected a s...<class 'int'>"
E         
E         - Expected a string, but got <class 'int'>
E         + expected string or bytes-like object, got 'int'

isort/Test4DT_tests/test_isort_parse_normalize_line_2_test_error_handling_invalid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_2_test_error_handling_invalid_input.py::test_normalize_line[from .cimport numpy-from  cimport numpy-from .cimport numpy]
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_2_test_error_handling_invalid_input.py::test_normalize_line[from .. import math-from  import math-from .. import math]
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_2_test_error_handling_invalid_input.py::test_normalize_line[\tfrom   numpy import sqrt-\tfrom   numpy import sqrt-\tfrom   numpy import sqrt]
============================== 3 failed in 0.12s ===============================
"""