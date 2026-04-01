
from pytutils.lazy.lazy_import import ImportReplacer
import pytest

@pytest.mark.parametrize("module_path, member, children", [
    (['foo'], 'bar', {'baz':(['foo', 'baz'], None, {})})
])
def test_error_case_invalid_both_member_and_children(module_path, member, children):
    with pytest.raises(ValueError) as e:
        ImportReplacer(scope=globals(), name='foo', module_path=module_path, member=member, children=children)
    assert str(e.value) == 'Cannot supply both a member and children'
