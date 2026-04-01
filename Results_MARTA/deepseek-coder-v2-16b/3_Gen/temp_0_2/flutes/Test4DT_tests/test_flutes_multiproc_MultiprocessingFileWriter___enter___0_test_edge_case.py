
import pytest
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def setup_writer():
    return MultiprocessingFileWriter('testfile.log')

def test_edge_case(setup_writer):
    writer = setup_writer
    assert isinstance(writer, MultiprocessingFileWriter)
