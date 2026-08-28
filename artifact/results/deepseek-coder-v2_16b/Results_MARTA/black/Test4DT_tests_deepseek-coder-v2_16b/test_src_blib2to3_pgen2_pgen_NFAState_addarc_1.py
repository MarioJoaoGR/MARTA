
import pytest
from typing import Optional, Text, List, Tuple

class NFAState:
    def __init__(self) -> None:
        self.arcs = []  # list of (label, NFAState) pairs
    
    def addarc(self, next: "NFAState", label: Optional[Text] = None) -> None:
        assert label is None or isinstance(label, str)
        assert isinstance(next, NFAState)
        self.arcs.append((label, next))

def test_valid_addarc():
    state = NFAState()
    next_state = NFAState()
    state.addarc(next_state, 'a')
    assert len(state.arcs) == 1
    assert state.arcs[0] == ('a', next_state)


def test_none_label():
    state = NFAState()
    next_state = NFAState()
    state.addarc(next_state, None)
    assert len(state.arcs) == 1
    assert state.arcs[0] == (None, next_state)