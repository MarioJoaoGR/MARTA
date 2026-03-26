
import pytest
from typing import Tuple, List, Callable

# Assuming Pos is a type that supports indexing and incrementation
Pos = int
ParseFloat = Callable[[str], float]

def parse_array(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, list]:
    pos += 1
    array: List[any] = []

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

def parse_value(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, any]:
    if src.startswith("null", pos):
        return pos + 4, None
    elif src.startswith('"', pos) or src.startswith("'", pos):
        return parse_string(src, pos)
    elif src[pos].isdigit() or (src[pos] == "-" and len(src) > pos + 1 and src[pos + 1].isdigit()):
        return parse_number(src, pos, parse_float)
    elif src[pos] == "[":
        return parse_array(src, pos, parse_float)[0], parse_array(src, pos, parse_float)[1]
    else:
        raise ValueError(f"Unexpected token at position {pos}: {src[pos]}")

def parse_number(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, float]:
    start = pos
    while pos < len(src) and (src[pos].isdigit() or src[pos] == "." or src[pos] == "-"):
        pos += 1
    if pos > start and isinstance(parse_float, Callable):
        return pos, parse_float(src[start:pos])
    else:
        return pos, int(src[start:pos])

def parse_string(src: str, pos: Pos) -> Tuple[Pos, str]:
    start = pos
    while pos < len(src) and src[pos] != '"' and src[pos] != "'":
        pos += 1
    if pos == len(src):
        raise ValueError("Unterminated string")
    return pos + 1, src[start+1:pos]

def suffixed_err(src: str, pos: Pos, msg: str) -> Exception:
    while pos > 0 and not src[pos-1].isspace():
        pos -= 1
    while pos < len(src) and not src[pos].isspace():
        pos += 1
    return ValueError(f"{msg} at position {pos}: {src[pos]}")

@pytest.mark.parametrize("src, expected", [('[]', [])])
def test_edge_case_empty_array(src: str, expected: List):
    pos = 0
    parse_float = float
    result = parse_array(src, pos, parse_float)
    assert result[1] == expected
