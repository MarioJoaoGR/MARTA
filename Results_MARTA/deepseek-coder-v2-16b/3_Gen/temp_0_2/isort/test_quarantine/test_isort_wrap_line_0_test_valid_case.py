
import pytest
from isort.wrap import Config, DEFAULT_CONFIG, Modes, line

@pytest.mark.parametrize("content, line_separator, config, expected", [
    ("This is a long line of text that needs to be wrapped.", " \\n", DEFAULT_CONFIG, "This is a long line of text that nee\\ds to be wrapped."),
])
def test_valid_case(content, line_separator, config, expected):
    assert line(content, line_separator, config) == expected

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

isort/Test4DT_tests/test_isort_wrap_line_0_test_valid_case.py F          [100%]

=================================== FAILURES ===================================
_ test_valid_case[This is a long line of text that needs to be wrapped.- \\n-config0-This is a long line of text that nee\\ds to be wrapped.] _

content = 'This is a long line of text that needs to be wrapped.'
line_separator = ' \\n'
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.tox', 'node_modules', '.bzr', '.pytype', 'venv', ...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
expected = 'This is a long line of text that nee\\ds to be wrapped.'

    @pytest.mark.parametrize("content, line_separator, config, expected", [
        ("This is a long line of text that needs to be wrapped.", " \\n", DEFAULT_CONFIG, "This is a long line of text that nee\\ds to be wrapped."),
    ])
    def test_valid_case(content, line_separator, config, expected):
>       assert line(content, line_separator, config) == expected
E       AssertionError: assert 'This is a lo...o be wrapped.' == 'This is a lo...o be wrapped.'
E         
E         - This is a long line of text that nee\ds to be wrapped.
E         ?                                     -
E         + This is a long line of text that needs to be wrapped.

isort/Test4DT_tests/test_isort_wrap_line_0_test_valid_case.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_line_0_test_valid_case.py::test_valid_case[This is a long line of text that needs to be wrapped.- \\n-config0-This is a long line of text that nee\\ds to be wrapped.]
============================== 1 failed in 0.09s ===============================
"""