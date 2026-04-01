
import pytest
from sty import primitive

def test_unmute():
    register = primitive.Register()
    assert not register.is_muted, "The register should be initially muted."
    
    # Unmuting the register
    register.unmute()
    assert not register.is_muted, "After unmuting, the register should still not be muted."
