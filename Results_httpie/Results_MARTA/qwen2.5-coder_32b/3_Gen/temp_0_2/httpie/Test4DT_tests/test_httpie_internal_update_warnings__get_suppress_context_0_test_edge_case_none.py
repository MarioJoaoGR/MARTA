
from unittest.mock import patch, MagicMock
import httpie.internal.update_warnings as update_warnings
from contextlib import nullcontext, suppress

def test_edge_case_none():
    # Create a mock Environment object with developer_mode set to False
    env = MagicMock()
    env.config.developer_mode = False
    
    # Call the function under test
    ctx_mgr = update_warnings._get_suppress_context(env)
    
    # Assert that the context manager is a suppressor of BaseException errors
    assert isinstance(ctx_mgr, suppress)
    
    # Create a mock Environment object with developer_mode set to True
    env.config.developer_mode = True
    
    # Call the function under test again
    ctx_mgr = update_warnings._get_suppress_context(env)
    
    # Assert that the context manager is a no-op (nullcontext)
    assert isinstance(ctx_mgr, nullcontext)
