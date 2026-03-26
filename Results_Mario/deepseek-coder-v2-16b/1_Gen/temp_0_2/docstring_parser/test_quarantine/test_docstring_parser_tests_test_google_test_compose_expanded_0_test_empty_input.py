
import pytest
from docstring_parser.tests.test_google import compose, parse, RenderingStyle

@pytest.mark.parametrize("source, expected", [
    ("""
    A brief description.
    
    Longer description that spans multiple lines.
    
    Args:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
    
    Returns:
        ReturnType: Description of the return value.
    """, "Expected expanded format...")
])
def test_compose_expanded(source, expected):
    assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_empty_input.py F [100%]

=================================== FAILURES ===================================
_ test_compose_expanded[\n    A brief description.\n    \n    Longer description that spans multiple lines.\n    \n    Args:\n        param1 (type): Description of param1.\n        param2 (type): Description of param2.\n    \n    Returns:\n        ReturnType: Description of the return value.\n    -Expected expanded format...] _

source = '\n    A brief description.\n    \n    Longer description that spans multiple lines.\n    \n    Args:\n        param1 ... param2 (type): Description of param2.\n    \n    Returns:\n        ReturnType: Description of the return value.\n    '
expected = 'Expected expanded format...'

    @pytest.mark.parametrize("source, expected", [
        ("""
        A brief description.
    
        Longer description that spans multiple lines.
    
        Args:
            param1 (type): Description of param1.
            param2 (type): Description of param2.
    
        Returns:
            ReturnType: Description of the return value.
        """, "Expected expanded format...")
    ])
    def test_compose_expanded(source, expected):
>       assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected
E       AssertionError: assert 'A brief desc...return value.' == 'Expected expanded format...'
E         
E         - Expected expanded format...
E         + A brief description.
E         + 
E         + Longer description that spans multiple lines.
E         + 
E         + Args:...
E         
E         ...Full output truncated (8 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_empty_input.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_empty_input.py::test_compose_expanded[\n    A brief description.\n    \n    Longer description that spans multiple lines.\n    \n    Args:\n        param1 (type): Description of param1.\n        param2 (type): Description of param2.\n    \n    Returns:\n        ReturnType: Description of the return value.\n    -Expected expanded format...]
============================== 1 failed in 0.03s ===============================
"""