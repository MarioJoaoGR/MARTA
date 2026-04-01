
import pytest
from isort._vendored.tomli._parser import parse_array
from isort._vendored.tomli._parser import Pos
from typing import Tuple, Callable

ParseFloat = Callable[[str], float]

def skip_comments_and_array_ws(src: str, pos: int) -> int:
    while pos < len(src):
        if src[pos] == " ":
            pos += 1
        elif src[pos] == "#":
            while pos < len(src) and src[pos] != "\n":
                pos += 1
        else:
            break
    return pos

def parse_value(src: str, pos: int, parse_float: ParseFloat) -> Tuple[int, any]:
    if src.startswith("\"", pos):
        start = pos
        while pos < len(src) and (src[pos] != "\"" or src[pos-1:pos+1] == "\\\"") :
            pos += 1
        if pos >= len(src):
            raise ValueError("Unterminated string")
        val = src[start+1:pos].replace("\\\"", "\"")
        return pos + 1, val
    elif src.startswith("[", pos) and src[pos] != "[":
        start = pos
        depth = 0
        while pos < len(src):
            if src[pos] == "[":
                depth += 1
            elif src[pos] == "]":
                depth -= 1
            pos += 1
            if depth == 0:
                break
        return pos, parse_array(src[start+1:pos-1], start + 1, parse_float)[1]
    else:
        raise ValueError("Invalid value")

# Test case for invalid input
def test_error_case_invalid_input():
    with pytest.raises(ValueError):
        src = "["
        pos = 0
        parse_float = float
        result = parse_array(src, pos, parse_float)
