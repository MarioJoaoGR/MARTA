
import pytest
from thefuck.rules.scm_correction import get_new_command



def test_invalid_input():
    with pytest.raises(AttributeError):
        get_new_command(None)