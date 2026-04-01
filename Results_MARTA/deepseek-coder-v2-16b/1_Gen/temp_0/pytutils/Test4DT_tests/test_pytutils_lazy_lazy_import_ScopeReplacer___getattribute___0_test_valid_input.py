
from pytutils.lazy.lazy_import import ScopeReplacer

def test_valid_input():
    class RealObject:
        def __init__(self, value):
            self.value = value

    scope = {}
    factory = lambda self, s, n: RealObject(n)
    replacer = ScopeReplacer(scope, factory, 'real_obj')

    # At this point, `replacer` is a placeholder in the scope, and accessing its attributes will trigger creation of the real object.
    assert isinstance(scope['real_obj'], RealObject)
    assert scope['real_obj'].value == 'real_obj'
