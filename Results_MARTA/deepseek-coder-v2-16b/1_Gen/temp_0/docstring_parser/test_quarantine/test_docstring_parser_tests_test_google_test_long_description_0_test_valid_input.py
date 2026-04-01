
import pytest
from docstring_parser.tests.test_google import parse

@pytest.mark.parametrize(
    "source, expected_short_desc, expected_long_desc, expected_blank",
    [
        (
            """This is a summary.
            
            Args:
                param1 (int): Description of parameter 1.
                param2 (str): Description of parameter 2.
                
            Returns:
                int: The result of the operation, which could be an integer.""",
            "This is a summary.",
            """Args:
    param1 (int): Description of parameter 1.
    param2 (str): Description of parameter 2.

Returns:
    int: The result of the operation, which could be an integer.""",
            True
        )
    ]
)
def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank
    assert not docstring.meta

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_ test_long_description[This is a summary.\n            \n            Args:\n                param1 (int): Description of parameter 1.\n                param2 (str): Description of parameter 2.\n                \n            Returns:\n                int: The result of the operation, which could be an integer.-This is a summary.-Args:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.-True] _

source = 'This is a summary.\n            \n            Args:\n                param1 (int): Description of parameter 1.\n     ...\n                \n            Returns:\n                int: The result of the operation, which could be an integer.'
expected_short_desc = 'This is a summary.'
expected_long_desc = 'Args:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.'
expected_blank = True

    @pytest.mark.parametrize(
        "source, expected_short_desc, expected_long_desc, expected_blank",
        [
            (
                """This is a summary.
    
                Args:
                    param1 (int): Description of parameter 1.
                    param2 (str): Description of parameter 2.
    
                Returns:
                    int: The result of the operation, which could be an integer.""",
                "This is a summary.",
                """Args:
        param1 (int): Description of parameter 1.
        param2 (str): Description of parameter 2.
    
    Returns:
        int: The result of the operation, which could be an integer.""",
                True
            )
        ]
    )
    def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
>       assert docstring.long_description == expected_long_desc
E       AssertionError: assert None == 'Args:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.'
E        +  where None = <docstring_parser.common.Docstring object at 0x103d34c10>.long_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_valid_input.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_valid_input.py::test_long_description[This is a summary.\n            \n            Args:\n                param1 (int): Description of parameter 1.\n                param2 (str): Description of parameter 2.\n                \n            Returns:\n                int: The result of the operation, which could be an integer.-This is a summary.-Args:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.-True]
============================== 1 failed in 0.03s ===============================

"""