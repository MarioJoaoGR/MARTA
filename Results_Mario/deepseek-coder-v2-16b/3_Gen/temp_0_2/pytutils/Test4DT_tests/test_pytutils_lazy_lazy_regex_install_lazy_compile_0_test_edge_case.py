
import pytest
from pytutils.lazy.lazy_regex import lazy_compile, reset_compile

def test_edge_case():
    import re
    
    # Before calling install_lazy_compile()
    assert not callable(re.compile) or re.compile != lazy_compile
    
    from pytutils.lazy.lazy_regex import install_lazy_compile
    install_lazy_compile()
    
    # After calling install_lazy_compile()
    assert callable(re.compile) and re.compile == lazy_compile
    
    reset_compile()
    
    # After calling reset_compile()
    assert not callable(re.compile) or re.compile != lazy_compile
