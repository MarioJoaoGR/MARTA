
import pytest
from docstring_parser.tests.test_google import parse, compose

@pytest.mark.parametrize("source, expected", [
    ("def example():\\n    \\\"\\\"\\\"This is a summary.\\n\\n    Args:\\n        arg1 (int): The first argument.\\n        arg2 (str): The second argument.\\n\\n    Returns:\\n        int: The result of the function.\\n    \\\"\\\"\\\"", "This is a summary.\n\nArgs:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function."),
])
def test_compose(source, expected):
    assert compose(parse(source)) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_0_test_empty_input.py F [100%]

=================================== FAILURES ===================================
_ test_compose[def example():\\n    \\"\\"\\"This is a summary.\\n\\n    Args:\\n        arg1 (int): The first argument.\\n        arg2 (str): The second argument.\\n\\n    Returns:\\n        int: The result of the function.\\n    \\"\\"\\"-This is a summary.\n\nArgs:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function.] _

source = 'def example():\\n    \\"\\"\\"This is a summary.\\n\\n    Args:\\n        arg1 (int): The first argument.\\n        arg2 (str): The second argument.\\n\\n    Returns:\\n        int: The result of the function.\\n    \\"\\"\\"'
expected = 'This is a summary.\n\nArgs:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function.'

    @pytest.mark.parametrize("source, expected", [
        ("def example():\\n    \\\"\\\"\\\"This is a summary.\\n\\n    Args:\\n        arg1 (int): The first argument.\\n        arg2 (str): The second argument.\\n\\n    Returns:\\n        int: The result of the function.\\n    \\\"\\\"\\\"", "This is a summary.\n\nArgs:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function."),
    ])
    def test_compose(source, expected):
>       assert compose(parse(source)) == expected
E       assert 'def example(...    \\"\\"\\"' == 'This is a su...the function.'
E         
E         + def example():\n    \"\"\"This is a summary.\n\n    Args:\n        arg1 (int): The first argument.\n        arg2 (str): The second argument.\n\n    Returns:\n        int: The result of the function.\n    \"\"\"
E         - This is a summary.
E         - 
E         - Args:
E         -     arg1 (int): The first argument.
E         -     arg2 (str): The second argument....
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_0_test_empty_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_0_test_empty_input.py::test_compose[def example():\\n    \\"\\"\\"This is a summary.\\n\\n    Args:\\n        arg1 (int): The first argument.\\n        arg2 (str): The second argument.\\n\\n    Returns:\\n        int: The result of the function.\\n    \\"\\"\\"-This is a summary.\n\nArgs:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function.]
============================== 1 failed in 0.03s ===============================
"""