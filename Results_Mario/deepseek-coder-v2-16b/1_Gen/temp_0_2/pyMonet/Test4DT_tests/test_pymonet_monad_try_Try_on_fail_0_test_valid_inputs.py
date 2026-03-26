
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    try_instance = Try(value='some_value', is_success=True)
    
    def fail_callback(val):
        assert False, "Expected no failure callback"
    
    # Ensure that the on_fail method does not call the fail_callback when is_success is True
    try_instance.on_fail(fail_callback)
