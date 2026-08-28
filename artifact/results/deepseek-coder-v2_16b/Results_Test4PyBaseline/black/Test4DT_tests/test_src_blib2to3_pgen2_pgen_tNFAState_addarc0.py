# Module: blib2to3.pgen2.pgen
import pytest
from typing import Optional, Text, List, Tuple

class NFAState:
    def __init__(self) -> None:
        self.arcs = []  # list of (label, NFAState) pairs
    
    def addarc(self, next: "NFAState", label: Optional[Text] = None) -> None:
        assert label is None or isinstance(label, str)
        assert isinstance(next, NFAState)
        self.arcs.append((label, next))

# Test cases for the NFAState class and its methods
def test_nfastate_initialization():
    nfa_state = NFAState()
    assert len(nfa_state.arcs) == 0, "Expected an empty list of arcs after initialization"

def test_addarc_with_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2, "a")
    assert len(state1.arcs) == 1, "Expected one arc after adding with label 'a'"
    assert state1.arcs[0][0] == "a", "Expected the added arc to have label 'a'"
    assert state1.arcs[0][1] is state2, "Expected the added arc to point to state2"

def test_addarc_without_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2)
    assert len(state1.arcs) == 1, "Expected one arc after adding without label"
    assert state1.arcs[0][0] is None, "Expected the added arc to have no label"
    assert state1.arcs[0][1] is state2, "Expected the added arc to point to state2"

def test_addarc_invalid_next():
    with pytest.raises(AssertionError):
        nfa_state = NFAState()
        nfa_state.addarc("not a valid next state")  # Invalid type for next

def test_addarc_invalid_label():
    state1 = NFAState()
    state2 = NFAState()
    with pytest.raises(AssertionError):
        state1.addarc(state2, 123)  # Invalid type for label (should be str or None)
