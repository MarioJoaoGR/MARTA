
import pytest
from semantic_release.hvcs import Gitlab
import os

def test_gitlab_token_retrieval():
    # Set a mock GL_TOKEN environment variable for testing
    os.environ["GL_TOKEN"] = "test_token"
    
    # Call the token method to retrieve the token
    token = Gitlab.token()
    
    # Assert that the retrieved token matches the expected value
    assert token == "test_token"

def test_gitlab_token_none():
    # Unset the GL_TOKEN environment variable for testing
    del os.environ["GL_TOKEN"]
    
    # Call the token method to retrieve the token
    token = Gitlab.token()
    
    # Assert that the retrieved token is None
    assert token is None
