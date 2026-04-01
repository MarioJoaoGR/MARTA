
from pytutils.lazy.lazy_import import ScopeReplacer

def test_invalid_input():
    scope = {}
    factory = lambda x, y, z: None  # Invalid factory function for testing
    
    try:
        replacer = ScopeReplacer(scope, factory, 'real_obj')
    except Exception as e:
        assert str(e) == "Invalid factory function provided"
