
import re
from dataclasses_json import snakecase as sc

def uplowcase(char, case):
    if case == 'up':
        return char.upper()
    elif case == 'low':
        return char.lower()
    else:
        raise ValueError("Invalid case argument")

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

def test_valid_input():
    assert sc("Hello, World!") == "hello_world"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_stringcase_snakecase_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_0_test_valid_input.py:3:0: E0611: No name 'snakecase' in module 'dataclasses_json' (no-name-in-module)


"""