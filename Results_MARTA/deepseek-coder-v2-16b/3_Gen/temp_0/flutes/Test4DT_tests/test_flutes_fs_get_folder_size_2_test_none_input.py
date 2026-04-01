
import pytest
from flutes.fs import get_folder_size
from pathlib import Path
import subprocess

@pytest.mark.skip(reason="This test will be enabled once the function is implemented")
def test_none_input():
    with pytest.raises(TypeError):
        assert get_folder_size(None) == 0
