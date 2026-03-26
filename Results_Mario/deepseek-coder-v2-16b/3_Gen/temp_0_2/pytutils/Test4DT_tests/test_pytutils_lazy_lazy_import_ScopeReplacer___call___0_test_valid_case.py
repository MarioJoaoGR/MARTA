
from pytutils.lazy.lazy_import import ScopeReplacer as RealObject

def test_valid_case():
    class MyRealObject:
        pass

    scope = {}
    factory = lambda obj, sc, nm: MyRealObject()  # Example factory function

    replacer = RealObject(scope, factory, 'real_obj')
    
    assert 'real_obj' in scope
    assert isinstance(scope['real_obj'], MyRealObject)
