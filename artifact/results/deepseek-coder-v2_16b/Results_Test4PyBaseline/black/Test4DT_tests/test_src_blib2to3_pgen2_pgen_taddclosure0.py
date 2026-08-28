# Module: blib2to3.pgen2.pgen
import pytest
from typing import Dict

class NFAState:
    def __init__(self):
        self.arcs = []  # list of (label, NFAState) pairs

    def addarc(self, next: "NFAState", label: str = None) -> None:
        assert isinstance(next, NFAState)
        self.arcs.append((label, next))

def addclosure(state: NFAState, base: Dict[NFAState, int]) -> None:
    assert isinstance(state, NFAState)
    if state in base:
        return
    base[state] = 1
    for label, next in state.arcs:
        if label is None:
            addclosure(next, base)

# Test cases
def test_addclosure_basic():
    nfa_state = NFAState()
    base = {}  # Dictionary to keep track of visited states
    addclosure(nfa_state, base)
    assert len(base) == 1
    assert nfa_state in base

def test_addclosure_existing_state():
    nfa_state1 = NFAState()
    nfa_state2 = NFAState()
    base = {nfa_state1: 1}  # Dictionary to keep track of visited states
    addclosure(nfa_state2, base)
    assert len(base) == 2
    assert nfa_state1 in base
    assert nfa_state2 in base

def test_addclosure_multiple_states():
    nfa_state1 = NFAState()
    nfa_state2 = NFAState()
    nfa_state3 = NFAState()
    base = {}  # Dictionary to keep track of visited states
    addclosure(nfa_state1, base)
    assert len(base) == 1
    assert nfa_state1 in base
    addclosure(nfa_state2, base)
    assert len(base) == 2
    assert nfa_state2 in base
    addclosure(nfa_state3, base)
    assert len(base) == 3
    assert nfa_state3 in base

def test_addclosure_with_arcs():
    nfa_state = NFAState()
    next_state = NFAState()
    nfa_state.addarc(next_state, None)
    base = {}  # Dictionary to keep track of visited states
    addclosure(nfa_state, base)
    assert len(base) == 2
    assert nfa_state in base
    assert next_state in base

def test_addclosure_with_multiple_arcs():
    nfa_state = NFAState()
    next_state1 = NFAState()
    next_state2 = NFAState()
    nfa_state.addarc(next_state1, None)
    nfa_state.addarc(next_state2, None)
    base = {}  # Dictionary to keep track of visited states
    addclosure(nfa_state, base)
    assert len(base) == 3
    assert nfa_state in base
    assert next_state1 in base
    assert next_state2 in base

# Run the tests
if __name__ == "__main__":
    pytest.main()
