
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_valid_inputs():
    try:
        exc = IllegalUseOfScopeReplacer('example', 'This is an example of misuse.', 'Please check your inputs.')
    except IllegalUseOfScopeReplacer as e:
        assert str(e) == "ScopeReplacer object 'example' was used incorrectly: This is an example of misuse.: Please check your inputs."
