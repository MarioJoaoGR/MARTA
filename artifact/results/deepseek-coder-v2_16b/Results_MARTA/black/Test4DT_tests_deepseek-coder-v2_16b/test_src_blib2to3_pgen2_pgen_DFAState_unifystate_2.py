
import pytest
from typing import Dict, Text, Any

class NFAState:
    pass

class DFAState:
    def __init__(self, nfaset: Dict[NFAState, Any], final: NFAState) -> None:
        assert isinstance(nfaset, dict)
        assert isinstance(next(iter(nfaset)), NFAState)
        assert isinstance(final, NFAState)
        self.nfaset = nfaset
        self.isfinal = final in nfaset
        self.arcs = {}  # map from label to DFAState

    def unifystate(self, old: "DFAState", new: "DFAState") -> None:
        for label, next_state in self.arcs.items():
            if next_state is old:
                self.arcs[label] = new

# Test cases for DFAState class
def test_dfastate_initialization():
    nfa_state1 = NFAState()
    nfa_state2 = NFAState()
    nfaset = {nfa_state1: 'data1', nfa_state2: 'data2'}
    dfa_state = DFAState(nfaset, final=nfa_state2)
    
    assert isinstance(dfa_state.nfaset, dict)
    assert len(dfa_state.nfaset) == 2
    assert dfa_state.isfinal is True
    assert dfa_state.arcs == {}

def test_unifystate_method():
    nfa_state1 = NFAState()
    nfa_state2 = NFAState()
    nfaset1 = {nfa_state1: 'data1', nfa_state2: 'data2'}
    dfa_state1 = DFAState(nfaset1, final=nfa_state2)
    
    nfa_state3 = NFAState()
    nfa_state4 = NFAState()
    nfaset2 = {nfa_state3: 'data3', nfa_state4: 'data4'}
    dfa_state2 = DFAState(nfaset2, final=nfa_state4)
    
    old_dfa_state = DFAState({nfa_state1: 'data1'}, nfa_state1)
    new_dfa_state = DFAState({nfa_state3: 'data3'}, nfa_state3)
    
    dfa_state1.unifystate(old_dfa_state, new_dfa_state)
    
    assert len(dfa_state1.arcs) == 0
    
    # Ensure the old DFA state is replaced with the new one in arcs
    for label, next_state in dfa_state1.arcs.items():
        assert next_state != old_dfa_state
        assert next_state == new_dfa_state
