
from pytutils.lazy.lazy_import import ScopeReplacer

def test_valid_case():
    class RealObject:
        def __init__(self, value):
            self.value = value
    
    scope = {}
    factory = lambda obj, sc, nm: RealObject(nm)  # Example factory function

    replacer = ScopeReplacer(scope, factory, 'real_obj')

    assert 'real_obj' in scope
