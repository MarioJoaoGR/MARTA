
import inspect
from types import FrameType
from typing import Callable, cast, Any, TypeVar
from flutes.multiproc import _pool_fn_with_state  # Assuming this is the correct module for _pool_fn_with_state

R = TypeVar('R')

def test_valid_case():
    def compute_function(state: int, data: int) -> int:
        return state + data
    
    # Mocking a state object
    mock_state = 10
    
    # Setting up the local variables in the frame to mimic having '__state__' set
    frame = inspect.currentframe()
    frame.f_locals['__state__'] = mock_state
    
    result = _pool_fn_with_state(compute_function, 5)
    
    assert result == mock_state + 5
