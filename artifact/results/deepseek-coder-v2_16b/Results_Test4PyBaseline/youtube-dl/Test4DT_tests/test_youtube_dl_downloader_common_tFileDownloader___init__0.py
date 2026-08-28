
# Module: youtube_dl.downloader.common
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    # If the module is not found, skip these tests or handle appropriately
    @pytest.mark.skip(reason="file_downloader module not found")
    def test_file_downloader_init_default(): pass
    @pytest.mark.skip(reason="file_downloader module not found")
    def test_file_downloader_init_specific(): pass
    @pytest.mark.skip(reason="file_downloader module not found")
    def test_file_downloader_init_additional(): pass
else:
    # Test initialization with default parameters
    def test_file_downloader_init_default():
        ydl = YoutubeDL()
        params = {}
        downloader = FileDownloader(ydl, params)
        assert hasattr(downloader, 'ydl')
        assert hasattr(downloader, '_progress_hooks')
        assert hasattr(downloader, 'params')
        assert isinstance(downloader.ydl, YoutubeDL)
        assert downloader.params == {}
        assert len(downloader._progress_hooks) == 1
        assert callable(downloader._progress_hooks[0])

    # Test initialization with specific parameters
    def test_file_downloader_init_specific():
        ydl = YoutubeDL()
        params = {
            'verbose': True,          # Print additional info to stdout.
            'ratelimit': 10240,       # Download speed limit, in bytes/sec.
            'buffersize': 8192,        # Size of download buffer in bytes.
        }
        downloader = FileDownloader(ydl, params)
        assert hasattr(downloader, 'ydl')
        assert hasattr(downloader, '_progress_hooks')
        assert hasattr(downloader, 'params')
        assert isinstance(downloader.ydl, YoutubeDL)
        assert downloader.params == params
        assert len(downloader._progress_hooks) == 1
        assert callable(downloader._progress_hooks[0])

    # Test initialization with additional parameters
    def test_file_downloader_init_additional():
        ydl = YoutubeDL()
        params = {
            'verbose': True,          # Print additional info to stdout.
            'ratelimit': 10240,       # Download speed limit, in bytes/sec.
            'buffersize': 8192,        # Size of download buffer in bytes.
            'test': True,              # Download only first bytes to test the downloader.
        }
        downloader = FileDownloader(ydl, params)
        assert hasattr(downloader, 'ydl')
        assert hasattr(downloader, '_progress_hooks')
        assert hasattr(downloader, 'params')
        assert isinstance(downloader.ydl, YoutubeDL)
        assert downloader.params == params
        assert len(downloader._progress_hooks) == 1
        assert callable(downloader._progress_hooks[0])
