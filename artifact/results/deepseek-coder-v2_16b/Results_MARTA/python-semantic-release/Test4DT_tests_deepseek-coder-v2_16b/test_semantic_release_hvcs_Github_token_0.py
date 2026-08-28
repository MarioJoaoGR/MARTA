
import pytest
from semantic_release.hvcs import Github
import os

def test_github_token():
    # Set a mock GH_TOKEN environment variable for testing
    os.environ["GH_TOKEN"] = "mocked_token"
    
    # Call the token method to retrieve the token
    token = Github.token()
    
    # Assert that the retrieved token matches the mocked value
    assert token == "mocked_token"

def test_github_no_token():
    # Unset the GH_TOKEN environment variable for testing
    del os.environ["GH_TOKEN"]
    
    # Call the token method to retrieve the token
    token = Github.token()
    
    # Assert that the retrieved token is None when the environment variable is not set
    assert token is None
