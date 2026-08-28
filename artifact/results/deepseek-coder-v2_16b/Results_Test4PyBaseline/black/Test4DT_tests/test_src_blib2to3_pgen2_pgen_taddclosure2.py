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
def test_basic_usage():
    nfa_state = NFAState()
    base = {}  # Dictionary to keep track of visited states
    addclosure(nfa_state, base)
    assert len(base) == 1
    assert nfa_state in base

def test_with_pre_existing_state():
    nfa_state1 = NFAState()
    nfa_state2 = NFAState()
    base = {nfa_state1: 1}  # Dictionary to keep track of visited states
    addclosure(nfa_state2, base)
    assert len(base) == 2
    assert nfa_state1 in base
    assert nfa_state2 in base

def test_with_multiple_states():
    nfa_state1 = NFAState()
    nfa_state2 = NFAState()
    nfa_state3 = NFAState()
    base = {}  # Dictionary to keep track of visited states
    addclosure(nfa_state1, base)
    assert len(base) == 1
    assert nfa_state1 in base
    assert nfa_state2 not in base
    assert nfa_state3 not in base
