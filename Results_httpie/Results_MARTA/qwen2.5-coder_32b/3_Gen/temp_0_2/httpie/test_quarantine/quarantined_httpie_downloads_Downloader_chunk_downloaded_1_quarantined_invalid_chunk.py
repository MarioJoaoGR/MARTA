
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader
from your_module import Environment, DownloadStatus

@pytest.fixture
def setup_downloader():
    env = Environment(config={"network": "example.com"})
    output_file = MagicMock()
    downloader = Downloader(env=env, output_file=output_file, resume=True)
    return downloader

@pytest.mark.parametrize("chunk", [b'data', b'12345'])
def test_chunk_downloaded(setup_downloader, chunk):
    with patch('your_module.DownloadStatus.chunk_downloaded') as mock_chunk_downloaded:
        setup_downloader.chunk_downloaded(chunk)
        assert mock_chunk_downloaded.call_count == 1
        mock_chunk_downloaded.assert_called_with(len(chunk))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_downloads_Downloader_chunk_downloaded_1_test_invalid_chunk
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_Downloader_chunk_downloaded_1_test_invalid_chunk.py:5:0: E0401: Unable to import 'your_module' (import-error)


"""