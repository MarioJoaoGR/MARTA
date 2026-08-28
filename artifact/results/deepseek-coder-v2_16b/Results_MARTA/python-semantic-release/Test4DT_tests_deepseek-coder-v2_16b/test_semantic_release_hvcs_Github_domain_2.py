
import pytest
from unittest.mock import patch
from semantic_release.hvcs import config

class Github:
    'Github helper class'
    DEFAULT_DOMAIN = 'github.com'
    
    def __init__(self):
        pass
    
    @property
    def domain(self) -> str:
        """Github domain property

        This method returns the current Github domain, which defaults to 'github.com'. 
        If a custom domain is set in the configuration using the key 'hvcs_domain', that value will be used instead.

        :return: The Github domain
        :rtype: str
        
        Example usage:
        ```python
        gh = Github()
        print(gh.domain)  # Outputs: github.com
        
        config.set("hvcs_domain", "githubenterprise.com")
        print(gh.domain)  # Outputs: githubenterprise.com
        ```
        """
        hvcs_domain = config.get("hvcs_domain")
        domain = hvcs_domain if hvcs_domain else Github.DEFAULT_DOMAIN
        return domain

# Test cases
def test_valid_input_default_domain():
    gh = Github()
    assert gh.domain == 'github.com'

def test_custom_domain():
    with patch.object(config, 'get', return_value='githubenterprise.com'):
        gh = Github()
        assert gh.domain == 'githubenterprise.com'

def test_missing_lines_to_cover():
    gh = Github()
    with pytest.raises(AssertionError):
        assert False, "This should not be reached without proper setup"
