
from pytutils.lazy.lazy_import import ScopeReplacer, IllegalUseOfScopeReplacer

def test_invalid_input():
    scope = {}
    factory = lambda self, s, n: None  # Placeholder for actual object creation logic
    
    try:
        replacer = ScopeReplacer(scope, factory, 'real_obj')
        assert 'real_obj' not in scope  # The placeholder is initially bound to the real object.
    except AssertionError as e:
        print(f"AssertionError: {e}")
