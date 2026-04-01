
import pytest
from typing import Tuple, Callable

# Assuming Pos is a type hint that supports indexing and incrementation, typically an int or a custom class implementing these functionalities.
Pos = int
ParseFloat = Callable[[str], float]

def parse_array(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, list]:
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
            raise suffixed_err(src, pos, "Unclosed array")
        pos += 1

        pos = skip_comments_and_array_ws(src, pos)
        if src.startswith("]", pos):
            return pos + 1, array

def skip_comments_and_array_ws(src: str, pos: Pos) -> Pos:
    while pos < len(src) and src[pos].isspace():
        pos += 1
    if pos < len(src) and src[pos] == "#":
        while pos < len(src) and src[pos] != "\n":
            pos += 1
    return pos

def parse_value(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, float]:
    if src.startswith("null", pos):
        return pos + 4, None
    elif src.startswith('"', pos):
        start = pos
        while pos < len(src) and src[pos] != '"':
            pos += 1
        if pos == len(src):
            raise ValueError("Unterminated string")
        return pos + 1, src[start+1:pos]
    elif src.startswith("-", pos) or src[pos].isdigit():
        start = pos
        while pos < len(src) and (src[pos].isdigit() or src[pos] == "."):
            pos += 1
        return pos, parse_float(src[start:pos])
    else:
        raise ValueError("Unexpected token")

def suffixed_err(src: str, pos: Pos, msg: str) -> Exception:
    return ValueError(f"{msg} at position {pos} in '{src}'")

# Test function for test_valid_case_2
@pytest.mark.parametrize("src, expected", [("[1.1, 2.2, 3.3]", [1.1, 2.2, 3.3])])
def test_valid_case_2(src: str, expected: list):
    pos = 0
    parse_float = float
    result = parse_array(src, pos, parse_float)
    assert result[1] == expected
