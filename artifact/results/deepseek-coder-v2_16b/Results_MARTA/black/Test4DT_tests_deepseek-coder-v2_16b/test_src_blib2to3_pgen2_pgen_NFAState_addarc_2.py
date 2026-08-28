
import pytest
from typing import Optional, Text, List, Tuple

class NFAState:
    def __init__(self) -> None:
        self.arcs = []  # list of (label, NFAState) pairs
    
    def addarc(self, next: "NFAState", label: Optional[Text] = None) -> None:
        assert label is None or isinstance(label, str)
        assert isinstance(next, NFAState)
        self.arcs.append((label, next))

def test_valid_input():
    state = NFAState()
    next_state = NFAState()
    state.addarc(next_state, 'a')  # Providing a valid NFAState object as the next state should not raise an error
    assert len(state.arcs) == 1
    assert state.arcs[0][0] == 'a'
    assert isinstance(state.arcs[0][1], NFAState)


def test_none_label():
    state = NFAState()
    next_state = NFAState()
    state.addarc(next_state, None)  # Providing None as the label should not raise an error
    assert len(state.arcs) == 1
    assert state.arcs[0][0] is None
    assert isinstance(state.arcs[0][1], NFAState)