
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

@pytest.mark.parametrize("success", [True, False])
def test_upload_to_release_success(success):
    with patch('semantic_release.hvcs.get_hvcs') as mock_get_hvcs:
        mock_hvcs = MagicMock()
        mock_get_hvcs.return_value = mock_hvcs
        mock_hvcs.upload_dists.return_value = success

        result = upload_to_release('owner', 'repository', 'version', '/path/to/dist')
        assert result == success

@pytest.mark.parametrize("success", [True, False])
def test_upload_to_release_failure(success):
    with patch('semantic_release.hvcs.get_hvcs') as mock_get_hvcs:
        mock_hvcs = MagicMock()
        mock_get_hvcs.return_value = mock_hvcs
        mock_hvcs.upload_dists.return_value = not success

        result = upload_to_release('owner', 'repository', 'version', '/path/to/dist')
        assert result == not success

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 37, col 26)
        assert result == not success
"""