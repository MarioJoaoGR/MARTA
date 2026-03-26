
import pytest
from pytutils.lazy.lazy_import import ImportReplacer

# Example 1: Importing a Module
def test_import_module():
    import_replacer = ImportReplacer(scope=globals(), name='foo', module_path=['bzrlib', 'foo'])
    assert 'foo' in globals()

# Example 2: Importing a Specific Member of a Module
def test_import_specific_member():
    import_replacer = ImportReplacer(scope=globals(), name='foo', module_path=['bzrlib', 'foo'], member='bar')