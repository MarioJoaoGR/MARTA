
import pytest
from typing import Optional, Text, List, Tuple

class NFAState:
    """
    Represents a state in a Non-deterministic Finite Automaton (NFA).
    
    Attributes:
        arcs (List[Tuple[Optional[Text], 'NFAState']]): A list of tuples where each tuple contains an optional label and a reference to another NFAState.
    
    Methods:
        __init__(): Initializes the NFA state with an empty list of arcs.
    
    Examples:
        Creating an instance of NFAState::
            nfa_state = NFAState()
        
        Adding arcs to the state::
            next_state1 = NFAState()
            nfa_state.arcs.append((None, next_state1))  # adding a transition with no label to next_state1
            
            next_state2 = NFAState()
            nfa_state.arcs.append(('a', next_state2))   # adding a transition with label 'a' to next_state2
    """
    def __init__(self) -> None:
        self.arcs = []  # list of (label, NFAState) pairs

# Test cases for NFAState class
def test_valid_init():
    nfa_state = NFAState()
    assert isinstance(nfa_state, NFAState), "Initialization with valid input should create an instance of NFAState"
    assert len(nfa_state.arcs) == 0, "Initial arcs list should be empty"

def test_add_arc():
    nfa_state = NFAState()
    next_state1 = NFAState()
    nfa_state.arcs.append((None, next_state1))
    
    assert len(nfa_state.arcs) == 1, "After adding one arc, the arcs list should have one element"
    assert nfa_state.arcs[0][0] is None, "The first arc should have no label"
    assert nfa_state.arcs[0][1] == next_state1, "The first arc should point to next_state1"
    
    next_state2 = NFAState()
    nfa_state.arcs.append(('a', next_state2))
    
    assert len(nfa_state.arcs) == 2, "After adding a second arc, the arcs list should have two elements"
    assert nfa_state.arcs[1][0] == 'a', "The second arc should have label 'a'"
    assert nfa_state.arcs[1][1] == next_state2, "The second arc should point to next_state2"

def test_invalid_init():
    with pytest.raises(TypeError):
        nfa_state = NFAState(1)  # Attempting to initialize with an invalid type
