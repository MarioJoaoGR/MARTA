
import pytest
from ansible.plugins.filter.core import regex_escape



def test_regex_escape_invalid_re_type():
    with pytest.raises(Exception) as e:
        result = regex_escape("Example", re_type='posix_extended')
    assert str(e.value) == "Regex type (posix_extended) not yet implemented"