
from isort._vendored.tomli._parser import Pos, ParseFloat, parse_value, skip_comments_and_array_ws
from typing import Tuple

def parse_array(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, list]:
    """Parses a JSON-like array from the given string `src` starting at position `pos`. The function iterates through the string to collect values into an array. It handles nested arrays and skips over comments and whitespace.

    Parameters:
        src (str): The input string containing the JSON-like array.
        pos (Pos): The current position in the string where parsing should start or continue. This is expected to be an instance of a class that supports indexing and incrementation, such as `int` or a custom class implementing these functionalities.
        parse_float (ParseFloat): A callable function used to convert string representations of numbers into their float equivalents.

    Returns:
        Tuple[Pos, list]: A tuple containing the updated position after parsing the array and the parsed array itself. The position is an instance of `Pos` representing the end of the parsed array in the input string.

    Examples:
        Example 1:
            src = "[1, 2, 3]"
            pos = 0
            parse_float = float
            result = parse_array(src, pos, parse_float)
            # The function will parse the array and update pos to 7 (the end of the array).
            print(result)  # Output: (7, [1, 2, 3])

        Example 2:
            src = "[1.1, 2.2, 3.3]"
            pos = 0
            parse_float = float
            result = parse_array(src, pos, parse_float)
            # The function will parse the array and update pos to 14 (the end of the array).
            print(result)  # Output: (14, [1.1, 2.2, 3.3])

        Example 3:
            src = "[\"apple\", \"banana\", \"cherry\"]"
            pos = 0
            parse_float = None
            result = parse_array(src, pos, parse_float)
            # The function will parse the array and update pos to 28 (the end of the array).
            print(result)  # Output: (28, ["apple", "banana", "cherry"])
    """
    pos += 1
    array: list = []

    pos = skip_comments_and_array_ws(src, pos)
    if src.startswith("]", pos):
        return pos + 1, array
    while True:
        pos, val = parse_value(src, pos, parse_float)
        array.append(val)
        pos = skip_comments_and_array_ws(src, pos)

        c = src[pos : pos + 1]
        if c == "]":
            return pos + 1, array
        if c != ",":
            raise ValueError("Unclosed array")
        pos += 1

        pos = skip_comments_and_array_ws(src, pos)
        if src.startswith("]", pos):
            return pos + 1, array

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.13s =============================
"""