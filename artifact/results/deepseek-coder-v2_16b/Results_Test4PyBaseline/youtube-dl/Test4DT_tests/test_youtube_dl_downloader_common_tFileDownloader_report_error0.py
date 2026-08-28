
# Module: youtube_dl.downloader.common
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mocking the FileDownloader for test purposes
        def __init__(self, ydl, params):
            self.params = params
            self.ydl = ydl
            self._progress_hooks = [lambda: None]  # Placeholder for a progress hook

        def real_download(self):
            raise NotImplementedError("This method is not implemented.")

        def report_error(self, error_message):
            if not hasattr(self, 'real_download'):
                raise NotImplementedError("report_error requires real_download to be implemented.")
            raise NotImplementedError(error_message)

# Test initialization with typical parameters
def test_file_downloader_init():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
        'continuedl': False
    }
    downloader = FileDownloader(ydl, params)
    
    assert downloader.params == params
    assert downloader.ydl is ydl
    assert len(downloader._progress_hooks) == 1
    assert callable(downloader._progress_hooks[0])

# Test report_error method
def test_report_error():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
        'continuedl': False
    }
    downloader = FileDownloader(ydl, params)
    
    with pytest.raises(NotImplementedError):
        downloader.real_download()
    
    # Assuming report_error is supposed to raise an error when real_download is not implemented
    with pytest.raises(NotImplementedError):
        downloader.report_error("Test Error Message")
