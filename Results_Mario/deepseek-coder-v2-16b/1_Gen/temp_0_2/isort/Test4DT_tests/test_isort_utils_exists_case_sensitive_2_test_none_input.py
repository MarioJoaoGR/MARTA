
import pytest
import os
import sys
from isort.utils import exists_case_sensitive

@pytest.mark.parametrize("input_path", [None])
def test_none_input(input_path):
    with pytest.raises(TypeError):
        assert not exists_case_sensitive(input_path)
