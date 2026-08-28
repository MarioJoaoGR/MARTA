
import pytest
from ast import Constant

def _e_type(*elements: list[list[Constant]]) -> str:
    """Get element type if type is constants."""
    if not elements:
        return ""
    ts = []
    for element in elements:
        if not element:
            ts.append("")
            continue
        t = ""
        for e in element:
            if not isinstance(e, Constant):
                t = "Any"
                break
            nw_t = type(e.value).__name__
            if t and t != nw_t:
                t = "Any"
                break
            t = nw_t
        ts.append(t)
    return '[' + ", ".join(ts) + ']'

def test_happy_path():
    result = _e_type([Constant(1), Constant(2)], [Constant('a'), Constant('b')])
    assert result == '[int, str]'

def test_edge_cases():
    result = _e_type([], [Constant(None)], [Constant(True), Constant(False)])
    assert result == '[, NoneType, bool]'

def test_invalid_inputs():
    result = _e_type([Constant(1), 2], [Constant('a'), 'b'])
    assert result == '[Any, Any]'
