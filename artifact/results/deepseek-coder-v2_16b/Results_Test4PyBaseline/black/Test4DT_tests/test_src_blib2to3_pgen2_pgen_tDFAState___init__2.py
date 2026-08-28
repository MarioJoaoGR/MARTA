
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
        return isinstance(other, DFAState) and self.isfinal == other.isfinal and self.arcs == other.arcs

# Example usage:
nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
dfa_state = DFAState(nfa_set, NFAState(2))

# Checking if the state is final
print(dfa_state.isfinal)  # Output: True or False depending on whether it's a final state

# Adding a transition from the current DFA state to another DFA state with label 'a'
next_state = DFAState({NFAState(3): 'c'}, NFAState(3))
dfa_state.addarc(next_state, 'a')

def test_initialization():
    nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
    final_state = NFAState(2)
    dfa_state = DFAState(nfa_set, final_state)
    
    assert isinstance(dfa_state.nfaset, dict), "nfaset should be a dictionary"
    assert all(isinstance(k, NFAState) for k in dfa_state.nfaset.keys()), "All keys in nfaset should be instances of NFAState"
    assert isinstance(final_state, NFAState), "Final state should be an instance of NFAState"
    assert dfa_state.isfinal == (final_state in nfa_set), "isfinal should reflect whether final is in nfaset"
    assert isinstance(dfa_state.arcs, dict), "arcs should be a dictionary"
    assert len(dfa_state.arcs) == 0, "Initial arcs length should be 0"

def test_addarc():
    nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
    final_state = NFAState(2)
    dfa_state = DFAState(nfa_set, final_state)
    
    next_state = DFAState({NFAState(3): 'c'}, NFAState(3))
    dfa_state.addarc(next_state, 'a')
    
    assert len(dfa_state.arcs) == 1, "Arcs length should be 1 after adding a new arc"
    assert 'a' in dfa_state.arcs, "'a' should be in arcs dictionary"
    assert dfa_state.arcs['a'] == next_state, "The destination state for label 'a' should match the provided next_state"

def test_unifystate():
    nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
    final_state = NFAState(2)
    dfa_state = DFAState(nfa_set, final_state)
    
    old_state = DFAState({NFAState(3): 'c'}, NFAState(3))
    new_state = DFAState({NFAState(4): 'd'}, NFAState(4))
    dfa_state.arcs['a'] = old_state
    
    dfa_state.unifystate(old_state, new_state)
    
    assert dfa_state.arcs['a'] == new_state, "The state with label 'a' should be unified to the new state"

def test_equality():
    nfa_set1 = {NFAState(1): 'a', NFAState(2): 'b'}
    final_state1 = NFAState(2)
    dfa_state1 = DFAState(nfa_set1, final_state1)
    
    nfa_set2 = {NFAState(1): 'a', NFAState(2): 'b'}
    final_state2 = NFAState(2)
    dfa_state2 = DFAState(nfa_set2, final_state2)
    
    assert dfa_state1 == dfa_state2, "Two DFA states with the same nfaset and final state should be equal"
    
    nfa_set3 = {NFAState(1): 'a', NFAState(3): 'b'}
    final_state3 = NFAState(3)
    dfa_state3 = DFAState(nfa_set3, final_state3)
    