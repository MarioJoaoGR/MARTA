
import pytest
from pytutils.lazy.lazy_import import ImportReplacer

def test_invalid_input_both_member_and_children():
    with pytest.raises(ValueError):
        ImportReplacer(scope={}, name='foo', module_path=['foo'], member='bar', children={'baz': (['foo'], None, {})})
