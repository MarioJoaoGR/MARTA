
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
                all(next_state1 is next_state2 for label, next_state1 in self.arcs.items() if (next_state2 := other.arcs.get(label)) is not None))

# Test cases for DFAState class
def test_dfa_state_initialization():
    nfa_set = {NFAState(1): 'a', NFAState(2): 'b'}
    dfa_state = DFAState(nfa_set, NFAState(2))
    assert isinstance(dfa_state.nfaset, dict)
    assert all(isinstance(k, NFAState) for k in dfa_state.nfaset.keys())
    assert isinstance(next(iter(dfa_state.nfaset)), NFAState)
    assert isinstance(dfa_state.isfinal, bool)