
import pytest
from unittest.mock import MagicMock, patch
from youtube_dl.downloader.common import FileDownloader


def test_report_file_already_downloaded_unicode_error():
    ydl = MagicMock()
    params = {}
    downloader = FileDownloader(ydl, params)
    
    with patch('builtins.print') as mock_print:
        # Simulate UnicodeEncodeError by mocking the to_screen method
        with patch.object(downloader, 'to_screen', side_effect=UnicodeEncodeError("ascii", "testfile", 0, len("testfile"), "ordinal not in range")):
            with pytest.raises(UnicodeEncodeError):
                downloader.report_file_already_downloaded("testfile")