
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

def test_init_default():
    nfa_state = NFAState()
    assert isinstance(nfa_state, NFAState), "Initialization should create an instance of NFAState"
    assert nfa_state.arcs == [], "Default initialization should have an empty list of arcs"

def test_add_arc():
    nfa_state = NFAState()
    next_state1 = NFAState()
    nfa_state.arcs.append((None, next_state1))
    assert len(nfa_state.arcs) == 1, "After adding an arc, the list of arcs should have one element"
    assert nfa_state.arcs[0][1] is next_state1, "The added arc should reference the correct NFAState"

def test_init_invalid():
    with pytest.raises(TypeError):
        NFAState('invalid_input')
