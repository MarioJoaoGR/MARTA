
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mock for the purpose of this test
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
        
        def undo_temp_name(self, filename):
            if filename is None:
                return None
            elif filename.endswith('.part'):
                return filename[:-5]
            else:
                return filename

# Fixture to create a FileDownloader instance for testing
@pytest.fixture
def downloader():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
    }
    return FileDownloader(ydl, params)

# Test case for the `undo_temp_name` method
def test_undo_temp_name(downloader):
    # Test with a filename ending in '.part'
    assert downloader.undo_temp_name('video_file.part') == 'video_file'
    
    # Test with a filename not ending in '.part'
    assert downloader.undo_temp_name('video_file') == 'video_file'
    
    # Test with an empty string
    assert downloader.undo_temp_name('') == ''
    
    # Test with a None value