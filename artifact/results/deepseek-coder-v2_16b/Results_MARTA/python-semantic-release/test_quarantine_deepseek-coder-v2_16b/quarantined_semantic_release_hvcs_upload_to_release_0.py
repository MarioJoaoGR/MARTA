
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_hvcs

def upload_to_release(owner: str, repository: str, version: str, path: str) -> bool:
    """
    Upload distributions to the current hvcs release API

    :param owner: The owner of the repository
    :param repository: The repository name
    :param version: A string with the version to upload for
    :param path: Path to dist directory

    :return: Status of the request
    """
    return get_hvcs().upload_dists(owner, repository, version, path)

# Test cases
def test_upload_to_release_basic():
    with patch('semantic_release.hvcs.get_hvcs') as mock_get_hvcs:
        mock_hvcs = MagicMock()
        mock_get_hvcs.return_value = mock_hvcs
        mock_hvcs.upload_dists.return_value = True

        result = upload_to_release('owner', 'repository', 'version', '/path/to/dist')
        assert result is True

def test_upload_to_release_with_config():
    with patch('semantic_release.hvcs.get_hvcs') as mock_get_hvcs:
        mock_hvcs = MagicMock()
        mock_get_hvcs.return_value = mock_hvcs
        mock_hvcs.upload_dists.return_value = True

        config = {'hvcs': 'MyHVCSHelper'}
        with patch('semantic_release.config', config):
            result = upload_to_release('owner', 'repository', 'version', '/path/to/dist')
            assert result is True

def test_upload_to_release_with_env_vars():
    with patch('os.environ', {'HVCS_TOKEN': 'your_token_here'}):
        result = upload_to_release('owner', 'repository', 'version', '/path/to/dist')
        assert result is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""