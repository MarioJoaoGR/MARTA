
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus
from io import BytesIO

@pytest.fixture
def valid_downloader():
    env = Environment(config={"network": "example.com"})
    output_file = BytesIO()
    return Downloader(env=env, output_file=output_file, resume=True)

def test_valid_inputs(valid_downloader):
    assert valid_downloader.finished is False
    assert isinstance(valid_downloader.status, DownloadStatus)
    assert valid_downloader._resume is True
    assert valid_downloader._resumed_from == 0
