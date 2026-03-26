
import pytest
from flutes.io import reverse_open
import io

@pytest.mark.parametrize("test_file, test_encoding, test_allow_empty_lines, test_buffer_size", [
    (None, None, False, None),
])
def test_edge_case(test_file, test_encoding, test_allow_empty_lines, test_buffer_size):
    with pytest.raises(TypeError):
        reverse_open(test_file, encoding=test_encoding, allow_empty_lines=test_allow_empty_lines, buffer_size=test_buffer_size)
