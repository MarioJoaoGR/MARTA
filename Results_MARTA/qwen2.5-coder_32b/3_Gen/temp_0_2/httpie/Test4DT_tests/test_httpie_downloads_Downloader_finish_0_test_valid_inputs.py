
from unittest.mock import patch, MagicMock
import httpie.downloads

class TestDownloader:
    @patch('httpie.downloads.Environment')
    def test_valid_inputs(self, MockEnv):
        mock_env = MockEnv()
        output_file = MagicMock()  # Using a MagicMock for the output file
        downloader = httpie.downloads.Downloader(env=mock_env, output_file=output_file)
    
        assert not downloader.finished
        with patch('httpie.downloads.DownloadStatus.finished') as mock_finish:
            downloader.finish()
            mock_finish.assert_called_once()
