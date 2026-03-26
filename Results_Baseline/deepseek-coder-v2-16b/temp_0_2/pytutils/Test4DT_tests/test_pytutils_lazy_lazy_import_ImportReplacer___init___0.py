# Module: pytutils.lazy.lazy_import
# test_lazy_import.py
from pytutils.lazy.lazy_import import ImportReplacer

def test_import_module_without_specifying_member():
    scope = globals()
    import_replacer = ImportReplacer(scope=scope, name='foo', module_path=['bzrlib', 'foo'])
    assert 'foo' in scope, "Module 'foo' should be imported into the global scope."

def test_import_specific_member_from_module():
    scope = globals()
    import_replacer = ImportReplacer(scope=scope, name='bar', module_path=['bzrlib', 'foo'], member='bar')
    assert 'bar' in scope, "Member 'bar' should be imported into the global scope."

def test_import_multiple_members_from_module():
    scope = globals()
    import_replacer = ImportReplacer(scope=scope, name='baz', module_path=['bzrlib', 'foo'], children={'bar': (['bzrlib', 'foo', 'bar'], None, {}), 'baz': (['bzrlib', 'foo', 'baz'], None, {})})
    assert 'bar' in scope, "Member 'bar' should be imported into the global scope."
    assert 'baz' in scope, "Member 'baz' should be imported into the global scope."

def test_import_module_with_children():
    scope = globals()
    import_replacer = ImportReplacer(scope=scope, name='foo', module_path=['bzrlib', 'foo'], children={'bar': (['bzrlib', 'foo', 'bar'], None, {}), 'baz': (['bzrlib', 'foo', 'baz'], None, {})})
    assert 'bar' in scope, "Member 'bar' should be imported into the global scope."
    assert 'baz' in scope, "Member 'baz' should be imported into the global scope."

def test_import_module_with_invalid_configuration():
    try:
        import_replacer = ImportReplacer(scope=globals(), name='foo', module_path=['bzrlib', 'foo'], member='bar', children={'baz': (['bzrlib', 'foo', 'baz'], None, {})})
    except ValueError as e:
        assert str(e) == "Cannot supply both a member and children", "Expected ValueError with the correct message."
