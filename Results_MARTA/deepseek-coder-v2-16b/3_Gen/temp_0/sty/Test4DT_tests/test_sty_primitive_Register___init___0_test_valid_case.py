
import pytest
from sty import Register  # Assuming 'sty' is the module and 'primitive' contains Renderfuncs

def test_register_initialization():
    register = Register()
    
    assert isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not register.is_muted, "Expected is_muted to be False"
    assert callable(register.eightbit_call), "Expected eightbit_call to be a callable"
    assert callable(register.rgb_call), "Expected rgb_call to be a callable"
    
    # Additional assertions for the lambda functions if needed
    assert register.eightbit_call(10) == 10, "Expected eightbit_call to return its input unchanged"
    assert register.rgb_call(255, 0, 0) == (255, 0, 0), "Expected rgb_call to return the RGB values passed"

if __name__ == "__main__":
    pytest.main()
