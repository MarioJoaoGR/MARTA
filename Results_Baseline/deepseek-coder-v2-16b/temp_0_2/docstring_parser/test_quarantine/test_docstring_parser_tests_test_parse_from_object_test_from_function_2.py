
import pytest
from docstring_parser import parse_from_object

def test_from_function():
    """Test the parsing of a function's docstring."""
    
    def a_function(param1: str, param2: int = 2):
        """Short description
        Args:
            param1: Description for param1
            param2: Description for param2
        """
        return f"{param1} {param2}"

    # Test the function definition itself to ensure it is correctly parsed
    expected_doc = "Short description\nArgs:\n    param1: Description for param1\n    param2: Description for param2"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_function_2.py F [100%]

=================================== FAILURES ===================================
______________________________ test_from_function ______________________________

    def test_from_function():
        """Test the parsing of a function's docstring."""
    
        def a_function(param1: str, param2: int = 2):
            """Short description
            Args:
                param1: Description for param1
                param2: Description for param2
            """
            return f"{param1} {param2}"
    
        # Test the function definition itself to ensure it is correctly parsed
        expected_doc = "Short description\nArgs:\n    param1: Description for param1\n    param2: Description for param2"
>       assert a_function.__doc__ == expected_doc, f"Expected docstring: {expected_doc}"
E       AssertionError: Expected docstring: Short description
E         Args:
E             param1: Description for param1
E             param2: Description for param2
E       assert 'Short descri...am2\n        ' == 'Short descri...on for param2'
E         
E           Short description
E         - Args:
E         +         Args:
E         -     param1: Description for param1
E         +             param1: Description for param1
E         ? ++++++++...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_function_2.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_function_2.py::test_from_function
============================== 1 failed in 0.02s ===============================

"""