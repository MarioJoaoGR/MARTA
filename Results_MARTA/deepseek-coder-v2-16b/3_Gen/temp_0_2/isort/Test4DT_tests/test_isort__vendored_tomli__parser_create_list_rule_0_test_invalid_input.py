
import pytest
from isort._vendored.tomli._parser import create_list_rule, Output, Pos, Key, skip_chars, TOML_WS, suffixed_err

@pytest.mark.parametrize("src", ["[[list]]\n[[list]]"])
def test_invalid_input(src):
    pos = 0
    with pytest.raises(TypeError) as excinfo:
        create_list_rule(src, pos, Output())
    assert "missing 2 required positional arguments" in str(excinfo.value)
