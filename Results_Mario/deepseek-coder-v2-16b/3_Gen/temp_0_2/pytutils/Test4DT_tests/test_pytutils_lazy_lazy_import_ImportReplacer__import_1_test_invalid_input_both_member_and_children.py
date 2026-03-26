
from pytutils.lazy.lazy_import import ImportReplacer
import pytest

@pytest.mark.parametrize("scope, name, module_path, member, children", [
    ({"foo": "bar"}, "baz", ["foo"], "bar", {"baz": (['foo'], None, {})})
])
def test_invalid_input_both_member_and_children(scope, name, module_path, member, children):
    with pytest.raises(ValueError) as e:
        ImportReplacer(scope, name, module_path, member=member, children=children)
    assert str(e.value) == 'Cannot supply both a member and children'
