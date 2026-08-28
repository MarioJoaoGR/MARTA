
# Module: youtube_dl.downloader.common
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    # If the module is not found, skip these tests or handle appropriately
    @pytest.mark.skip(reason="file_downloader module not found")
    def test_init_default_parameters(create_default_file_downloader): pass
    @pytest.mark.skip(reason="file_downloader module not found")
    def test_init_specific_parameters(create_specific_file_downloader): pass
    @pytest.mark.skip(reason="file_downloader module not found")
    def test_add_progress_hook(create_default_file_downloader): pass
    @pytest.mark.skip(reason="file_downloader module not found")
    def test_to_stderr(create_default_file_downloader): pass
else:
    # Fixture for creating a FileDownloader instance with default parameters
    @pytest.fixture
    def create_default_file_downloader():
        ydl = YoutubeDL()
        params = {}
        downloader = FileDownloader(ydl, params)
        return downloader

    # Fixture for creating a FileDownloader instance with specific parameters
    @pytest.fixture
    def create_specific_file_downloader():
        ydl = YoutubeDL()
        params = {
            'verbose': True,
            'ratelimit': 10240,
            'buffersize': 8192,
        }
        downloader = FileDownloader(ydl, params)
        return downloader

    # Test case for initializing the FileDownloader with default parameters
    def test_init_default_parameters(create_default_file_downloader):
        downloader = create_default_file_downloader
        assert hasattr(downloader, 'ydl')
        assert hasattr(downloader, '_progress_hooks')
        assert hasattr(downloader, 'params')
        assert downloader.params == {}

    # Test case for initializing the FileDownloader with specific parameters
    def test_init_specific_parameters(create_specific_file_downloader):
        downloader = create_specific_file_downloader
        assert hasattr(downloader, 'ydl')
        assert hasattr(downloader, '_progress_hooks')
        assert hasattr(downloader, 'params')
        assert downloader.params == {
            'verbose': True,
            'ratelimit': 10240,
            'buffersize': 8192,
        }

    # Test case for adding a progress hook to the FileDownloader instance
    def test_add_progress_hook(create_default_file_downloader):
        downloader = create_default_file_downloader
        assert len(downloader._progress_hooks) == 0
        downloader.add_progress_hook(lambda *args: None)
        assert len(downloader._progress_hooks) == 1

    # Test case for logging a message to stderr using the FileDownloader instance
    def test_to_stderr(create_default_file_downloader):
        downloader = create_default_file_downloader
        with pytest.raises(NotImplementedError):
            downloader.to_stderr("Test message")
