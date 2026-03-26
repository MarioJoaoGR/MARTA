
import pytest
from isort.parse import import_type, Config, DEFAULT_CONFIG

@pytest.mark.parametrize("line, expected", [
    ("import os", "straight"),
    ("from math import sin", "from"),
    ("import sys # isort:skip", None),
    ("cimport numpy as np", "straight"),
    ("# isort: skip", None),
    ("import os # noqa", None),
    ("from math import sin # isort:skip", None),
    ("# this is a comment", None),
    ("cimport numpy as np # isort:split", None),
])
def test_none_input(line, expected):
    assert import_type(line) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 9 items

isort/Test4DT_tests/test_isort_parse_import_type_1_test_none_input.py .. [ 22%]
...F..F                                                                  [100%]

=================================== FAILURES ===================================
____________________ test_none_input[import os # noqa-None] ____________________

line = 'import os # noqa', expected = None

    @pytest.mark.parametrize("line, expected", [
        ("import os", "straight"),
        ("from math import sin", "from"),
        ("import sys # isort:skip", None),
        ("cimport numpy as np", "straight"),
        ("# isort: skip", None),
        ("import os # noqa", None),
        ("from math import sin # isort:skip", None),
        ("# this is a comment", None),
        ("cimport numpy as np # isort:split", None),
    ])
    def test_none_input(line, expected):
>       assert import_type(line) == expected
E       AssertionError: assert 'straight' == None
E        +  where 'straight' = import_type('import os # noqa')

isort/Test4DT_tests/test_isort_parse_import_type_1_test_none_input.py:17: AssertionError
___________ test_none_input[cimport numpy as np # isort:split-None] ____________

line = 'cimport numpy as np # isort:split', expected = None

    @pytest.mark.parametrize("line, expected", [
        ("import os", "straight"),
        ("from math import sin", "from"),
        ("import sys # isort:skip", None),
        ("cimport numpy as np", "straight"),
        ("# isort: skip", None),
        ("import os # noqa", None),
        ("from math import sin # isort:skip", None),
        ("# this is a comment", None),
        ("cimport numpy as np # isort:split", None),
    ])
    def test_none_input(line, expected):
>       assert import_type(line) == expected
E       AssertionError: assert 'straight' == None
E        +  where 'straight' = import_type('cimport numpy as np # isort:split')

isort/Test4DT_tests/test_isort_parse_import_type_1_test_none_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_import_type_1_test_none_input.py::test_none_input[import os # noqa-None]
FAILED isort/Test4DT_tests/test_isort_parse_import_type_1_test_none_input.py::test_none_input[cimport numpy as np # isort:split-None]
========================= 2 failed, 7 passed in 0.12s ==========================
"""