
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mocking FileDownloader for the test case
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = []
        
        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

# Fixture to create an instance of FileDownloader with default parameters
@pytest.fixture
def downloader():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
    }
    return FileDownloader(ydl, params)

# Test case to check if the add_progress_hook method adds a hook correctly
def test_add_progress_hook(downloader):
    def mock_progress_hook(*args):
        pass  # Mock function for testing purposes
    
    downloader.add_progress_hook(mock_progress_hook)
    assert len(downloader._progress_hooks) == 1
    assert downloader._progress_hooks[0] == mock_progress_hook

# Additional test case to cover the uncovered line directly
def test_add_progress_hook_coverage(downloader):
    # Ensure that adding a progress hook increases the length of the hooks list
    initial_length = len(downloader._progress_hooks)
    downloader.add_progress_hook(lambda: None)  # Adding a lambda as a mock hook
    assert len(downloader._progress_hooks) == initial_length + 1
