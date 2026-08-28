
import pytest
from typing import Dict, Any, Text

class NFAState:
    def __init__(self, state_id: int):
        self.state_id = state_id

class DFAState:
    def __init__(self, nfaset: Dict[NFAState, Any], final: NFAState):
        assert isinstance(nfaset, dict)
        assert isinstance(next(iter(nfaset)), NFAState)
        assert isinstance(final, NFAState)
        self.nfaset = nfaset
        self.isfinal = final in nfaset
        self.arcs = {}  # map from label to DFAState

    def addarc(self, next: "DFAState", label: Text) -> None:
        assert isinstance(label, str)
        assert label not in self.arcs
        assert isinstance(next, DFAState)
        self.arcs[label] = next

    def unifystate(self, old: "DFAState", new: "DFAState") -> None:
        for label, next in self.arcs.items():
            if next is old:
                self.arcs[label] = new

    def __eq__(self, other: Any) -> bool:
        return (isinstance(other, DFAState) and 
                self.isfinal == other.isfinal and 
                len(self.arcs) == len(other.arcs) and 
                all(next_state1 == next_state2 for label, next_state1 in self.arcs.items() if (next_state2 := other.arcs.get(label)) is not None))

# Example usage:
nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
dfa_state = DFAState(nfa_set, NFAState(2))

# Checking if the state is final
print(dfa_state.isfinal)  # Output: True or False depending on whether it's a final state

# Adding a transition from the current DFA state to another DFA state with label 'a'
next_state = DFAState({NFAState(3): 'c'}, NFAState(3))
dfa_state.addarc(next_state, 'a')

# Test cases for DFAState class
def test_dfastate_initialization():
    nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
    final_nfa_state = NFAState(2)
    dfa_state = DFAState(nfa_set, final_nfa_state)
    
    assert isinstance(dfa_state.nfaset, dict)
    assert all(isinstance(key, NFAState) for key in dfa_state.nfaset)
    assert isinstance(dfa_state.isfinal, bool)
    assert dfa_state.isfinal == (final_nfa_state in nfa_set)
    assert isinstance(dfa_state.arcs, dict)
    assert len(dfa_state.arcs) == 0

def test_addarc():
    nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
    dfa_state = DFAState(nfa_set, NFAState(2))
    
    next_state = DFAState({NFAState(3): 'c'}, NFAState(3))
    dfa_state.addarc(next_state, 'a')
    
    assert len(dfa_state.arcs) == 1
    assert 'a' in dfa_state.arcs
    assert dfa_state.arcs['a'] == next_state

def test_unifystate():
    nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
    dfa_state = DFAState(nfa_set, NFAState(2))
    
    old_state = DFAState({NFAState(3): 'c'}, NFAState(3))
    new_state = DFAState({NFAState(4): 'd'}, NFAState(4))
    
    dfa_state.arcs['a'] = old_state
    dfa_state.unifystate(old_state, new_state)
    
    assert dfa_state.arcs['a'] == new_state

def test_equality():
    nfa_set1 = {NFAState(1): 'a', NFAState(2): 'b'}
    final_nfa_state1 = NFAState(2)
    dfa_state1 = DFAState(nfa_set1, final_nfa_state1)
    
    nfa_set2 = {NFAState(1): 'a', NFAState(2): 'b'}
    final_nfa_state2 = NFAState(2)
    dfa_state2 = DFAState(nfa_set2, final_nfa_state2)
    
    assert dfa_state1 == dfa_state2
    
    nfa_set3 = {NFAState(1): 'a', NFAState(3): 'b'}
    final_nfa_state3 = NFAState(3)
    dfa_state3 = DFAState(nfa_set3, final_nfa_state3)
    