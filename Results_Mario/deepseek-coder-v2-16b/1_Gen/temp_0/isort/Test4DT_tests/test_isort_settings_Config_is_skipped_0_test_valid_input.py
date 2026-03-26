
import pytest
from isort.settings import Config

@pytest.mark.parametrize("config_overrides", [
    {"quiet": True},
    {"profile": "black"},
    {"sections": ["third_party"]},
])
def test_valid_input(config_overrides):
    # Create a mock Config object with valid configuration settings
    config = Config(**config_overrides)
    
    # Add assertions to verify the configuration is set correctly
    assert hasattr(config, "quiet") and getattr(config, "quiet", False) == bool(config_overrides.get("quiet"))
    if "profile" in config_overrides:
        assert hasattr(config, "profile") and getattr(config, "profile", None) == config_overrides["profile"]
    if "sections" in config_overrides:
        assert hasattr(config, "sections") and getattr(config, "sections", ()) == tuple(config_overrides["sections"])
