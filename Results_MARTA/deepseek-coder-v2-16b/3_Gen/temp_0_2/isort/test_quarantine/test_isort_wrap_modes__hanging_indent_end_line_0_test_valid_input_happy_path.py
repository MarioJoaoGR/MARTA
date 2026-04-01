
# Import the hanging_indent_end_line function from isort.wrap_modes
from isort.wrap_modes import _hanging_indent_end_line

def test_valid_input_happy_path():
    # Test case for a line that does not end with a space
    assert _hanging_indent_end_line("This is a test") == "This is a test \\"
    
    # Test case for a line that already ends with a space
    assert _hanging_indent_end_line("This is a test ") == "This is a test  \\"
    
    # Test case for an empty line
    assert _hanging_indent_end_line("") == " \\"

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

isort/Test4DT_tests/test_isort_wrap_modes__hanging_indent_end_line_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test case for a line that does not end with a space
        assert _hanging_indent_end_line("This is a test") == "This is a test \\"
    
        # Test case for a line that already ends with a space
>       assert _hanging_indent_end_line("This is a test ") == "This is a test  \\"
E       AssertionError: assert 'This is a test \\' == 'This is a test  \\'
E         
E         - This is a test  \
E         ?                -
E         + This is a test \

isort/Test4DT_tests/test_isort_wrap_modes__hanging_indent_end_line_0_test_valid_input_happy_path.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes__hanging_indent_end_line_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.10s ===============================
"""