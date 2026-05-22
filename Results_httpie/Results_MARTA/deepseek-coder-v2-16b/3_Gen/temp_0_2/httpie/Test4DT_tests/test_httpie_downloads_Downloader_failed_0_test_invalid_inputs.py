
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader

@pytest.fixture
def downloader():
    env = MagicMock()
    output_file = MagicMock()
    return Downloader(env=env, output_file=output_file)

def test_invalid_inputs(downloader):
    with patch('httpie.downloads.Downloader.__init__', side_effect=TypeError("Invalid type for 'resume' parameter")):
        with pytest.raises(TypeError) as excinfo:
            Downloader(env=MagicMock(), output_file=MagicMock(), resume='invalid')
        assert str(excinfo.value) == "Invalid type for 'resume' parameter"
