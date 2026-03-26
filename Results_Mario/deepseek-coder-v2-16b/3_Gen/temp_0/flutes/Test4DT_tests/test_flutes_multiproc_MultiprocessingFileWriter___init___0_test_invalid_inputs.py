
import pytest
from flutes.multiproc import MultiprocessingFileWriter

def test_invalid_inputs():
    with pytest.raises(ValueError):
        writer = MultiprocessingFileWriter('non_existent_file', 'unsupported_mode')
