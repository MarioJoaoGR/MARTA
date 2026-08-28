
import pytest
from pytutils.lazy.lazy_import import ImportReplacer

# Test for valid direct import
def test_valid_direct_import():
    try:
        ImportReplacer(scope=globals(), name='foo', module_path=['bzrlib', 'foo'])
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

# Test for valid indirect import with member
def test_valid_indirect_import():
    try:
        ImportReplacer(scope=globals(), name='bar', module_path=['bzrlib', 'foo'], member='bar')
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

# Test for invalid both member and children
def test_invalid_both_member_and_children():
    with pytest.raises(ValueError):
        ImportReplacer(scope=globals(), name='baz', module_path=['bzrlib', 'foo'], member='bar', children={'bar':(['bzrlib', 'foo', 'bar'], None, {})})
