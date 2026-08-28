
import pytest
from semantic_release.dist import should_remove_dist

# Define a fixture for config to be used in tests
@pytest.fixture(scope="module")
def config():
    return {"remove_dist": "true"}

def test_should_remove_dist_true_config(config):
    # Set up a configuration that should return True
    config["remove_dist"] = "true"
    
    assert should_remove_dist() is True
