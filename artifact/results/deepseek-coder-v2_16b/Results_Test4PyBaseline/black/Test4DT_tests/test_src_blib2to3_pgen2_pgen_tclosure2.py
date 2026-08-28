# Module: blib2to3.pgen2.pgen
import pytest
from typing import Optional, Text, Dict

# Assuming the implementation of addclosure is provided elsewhere in your code
class NFAState:
    def __init__(self):
        self.arcs = []  # list of (label, NFAState) pairs
    
    def addarc(self, next: "NFAState", label: Optional[Text] = None) -> None:
        assert label is None or isinstance(label, str)
        assert isinstance(next, NFAState)
        self.arcs.append((label, next))

def closure(state: NFAState) -> Dict[NFAState, int]:
    base: Dict[NFAState, int] = {}
    addclosure(state, base)
    return base

# Assuming the implementation of addclosure is provided elsewhere in your code
def addclosure(state: NFAState, closure_set: Dict[NFAState, int]):
    # Example implementation of addclosure (not provided here)
    pass

# Example usage
if __name__ == "__main__":
    state = NFAState()  # Create an instance of NFAState
    result = closure(state)  # Compute the epsilon-closure of 'state'

# Test cases for closure function
def test_closure():
    state = NFAState()
    assert closure(state) == {}
