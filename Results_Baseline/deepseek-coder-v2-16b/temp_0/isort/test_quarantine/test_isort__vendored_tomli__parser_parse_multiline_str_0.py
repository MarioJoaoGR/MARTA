
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import parse_multiline_str

# Define a dummy Pos class to simulate the type hinting for position in the source string
class Pos:
    def __init__(self, value):
        self.value = value

# Test cases for parsing multi-line literal strings
@pytest.mark.parametrize("src, pos, expected_position, expected_string", [
    ("'''This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \\n and \\t.", 0, 51, "This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \n and \t."),
    ("'''This string contains special characters like \\n and \\t.", 0, 47, "This string contains special characters like \n and \t.")
])
def test_parse_multiline_literal(src, pos, expected_position, expected_string):
    literal = True
    parsed_position, parsed_string = parse_multiline_str(src, Pos(pos), literal=literal)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_ test_parse_multiline_literal['''This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \\n and \\t.-0-51-This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \n and \t.] _

src = "'''This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \\n and \\t."
pos = 0, expected_position = 51
expected_string = 'This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \n and \t.'

    @pytest.mark.parametrize("src, pos, expected_position, expected_string", [
        ("'''This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \\n and \\t.", 0, 51, "This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \n and \t."),
        ("'''This string contains special characters like \\n and \\t.", 0, 47, "This string contains special characters like \n and \t.")
    ])
    def test_parse_multiline_literal(src, pos, expected_position, expected_string):
        literal = True
>       parsed_position, parsed_string = parse_multiline_str(src, Pos(pos), literal=literal)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = "'''This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \\n and \\t."
pos = <Test4DT_tests.test_isort__vendored_tomli__parser_parse_multiline_str_0.Pos object at 0x7f1d5b2694d0>

    def parse_multiline_str(src: str, pos: Pos, *, literal: bool) -> Tuple[Pos, str]:
>       pos += 3
E       TypeError: unsupported operand type(s) for +=: 'Pos' and 'int'

isort/isort/_vendored/tomli/_parser.py:506: TypeError
_ test_parse_multiline_literal['''This string contains special characters like \\n and \\t.-0-47-This string contains special characters like \n and \t.] _

src = "'''This string contains special characters like \\n and \\t.", pos = 0
expected_position = 47
expected_string = 'This string contains special characters like \n and \t.'

    @pytest.mark.parametrize("src, pos, expected_position, expected_string", [
        ("'''This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \\n and \\t.", 0, 51, "This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \n and \t."),
        ("'''This string contains special characters like \\n and \\t.", 0, 47, "This string contains special characters like \n and \t.")
    ])
    def test_parse_multiline_literal(src, pos, expected_position, expected_string):
        literal = True
>       parsed_position, parsed_string = parse_multiline_str(src, Pos(pos), literal=literal)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = "'''This string contains special characters like \\n and \\t."
pos = <Test4DT_tests.test_isort__vendored_tomli__parser_parse_multiline_str_0.Pos object at 0x7f1d5b498550>

    def parse_multiline_str(src: str, pos: Pos, *, literal: bool) -> Tuple[Pos, str]:
>       pos += 3
E       TypeError: unsupported operand type(s) for +=: 'Pos' and 'int'

isort/isort/_vendored/tomli/_parser.py:506: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0.py::test_parse_multiline_literal['''This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \\n and \\t.-0-51-This is a multi-line literal string. It can contain multiple lines.\nWith special characters like \n and \t.]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0.py::test_parse_multiline_literal['''This string contains special characters like \\n and \\t.-0-47-This string contains special characters like \n and \t.]
============================== 2 failed in 0.11s ===============================
"""