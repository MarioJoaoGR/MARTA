
import pytest
from unittest.mock import patch, MagicMock
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

# Test scenarios
def test_valid_inputs():
    gh = Github()
    with patch('semantic_release.hvcs.config.get', return_value=None):
        assert gh.domain == 'github.com'
    with patch('semantic_release.hvcs.config.get', return_value='customdomain.com'):
        assert gh.domain == 'customdomain.com'

def test_edge_cases():
    gh = Github()
    with patch('semantic_release.hvcs.config.get', return_value=None):
        assert gh.domain == 'github.com'
    with patch('semantic_release.hvcs.config.get', side_effect=[None, None]):
        assert gh.domain == 'github.com'

def test_invalid_inputs():
    gh = Github()
    with pytest.raises(Exception):
        with patch('semantic_release.hvcs.config.get', side_effect=KeyError("No key found")):
            gh.domain
