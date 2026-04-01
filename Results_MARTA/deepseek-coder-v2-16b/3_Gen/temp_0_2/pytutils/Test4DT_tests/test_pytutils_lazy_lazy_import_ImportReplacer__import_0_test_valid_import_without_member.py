
from pytutils.lazy.lazy_import import ImportReplacer

def test_valid_import_without_member():
    scope = {}
    replacer = ImportReplacer(scope, 'foo', ['foo'])
    
    assert 'foo' in scope
    assert isinstance(scope['foo'], ImportReplacer)
