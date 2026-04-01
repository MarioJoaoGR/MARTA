
import pytest
from flutes.io import reverse_open
import io

@pytest.mark.parametrize("test_file, buffer_size", [(None, None)])
def test_edge_case(test_file, buffer_size):
    with pytest.raises(TypeError):
        for line in reverse_open(test_file, encoding='utf-8', allow_empty_lines=False, buffer_size=buffer_size):
            print(line)
