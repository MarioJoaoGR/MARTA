
import re
from dataclasses_json.stringcase import uplowcase

def snakecase(string):
    """Convert string into snake case.
    Join punctuation with underscore

    Args:
        string: String to convert.

    Returns:
        string: Snake cased string.

    """

    string = re.sub(r"[\-\.\s]", '_', str(string))
    if not string:
        return string
    return (uplowcase(string[0], 'low')
            + re.sub(r"[A-Z0-9]",
                     lambda matched: '_' + uplowcase(matched.group(0), 'low'),
                     string[1:]))

# Test case for valid input
def test_valid_input():
    assert snakecase("HelloWorld") == "hello_world"
    assert snakecase("Hello-World") == "hello_world"
    assert snakecase("Hello World") == "hello_world"
    assert snakecase("") == ""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        assert snakecase("HelloWorld") == "hello_world"
>       assert snakecase("Hello-World") == "hello_world"
E       AssertionError: assert 'hello__world' == 'hello_world'
E         
E         - hello_world
E         + hello__world
E         ?       +

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_1_test_valid_input.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""