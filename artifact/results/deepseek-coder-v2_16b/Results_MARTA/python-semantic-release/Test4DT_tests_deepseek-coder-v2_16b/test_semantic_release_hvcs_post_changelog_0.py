
import pytest
from semantic_release.hvcs import get_hvcs

def post_changelog(owner: str, repository: str, version: str, changelog: str) -> bool:
    """
    Posts the changelog to the current hvcs release API.

    This function sends a changelog entry for a specified version of a repository to the HVCS (Version Control System) release API. It requires the owner of the repository, the repository name, the new version, and the changelog content in the correct format. The function uses the `get_hvcs` method to retrieve the appropriate HVCS helper class based on the configuration and then calls its `post_release_changelog` method to post the changelog.

    Parameters:
        owner (str): The owner of the repository, which is typically a username or organization name.
        repository (str): The name of the repository where the changelog should be posted.
        version (str): A string representing the new version for which the changelog is being posted.
        changelog (str): A string containing the changelog content formatted appropriately for the HVCS release API.

    Returns:
        bool: A boolean indicating whether the changelog was successfully posted to the HVCS release API. The result will be `True` if successful, and `False` otherwise.
    """
    logger.debug(f"Posting release changelog for {owner}/{repository} {version}")
    return get_hvcs().post_release_changelog(owner, repository, version, changelog)

# Test cases


def test_invalid_inputs():
    hvcs = get_hvcs()
    hvcs.post_release_changelog = lambda owner, repo, version, changelog: False  # Mock the method to always return False
    
    with pytest.raises(NameError):
        result = post_changelog(owner="invalid_owner", repository="invalid_repo", version="invalid_version", changelog="invalid_changelog")