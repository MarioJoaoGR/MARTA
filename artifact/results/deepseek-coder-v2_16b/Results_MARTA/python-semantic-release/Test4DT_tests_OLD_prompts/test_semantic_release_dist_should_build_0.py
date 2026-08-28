
import pytest
from unittest.mock import patch
from semantic_release.dist import should_build

def test_valid_input_all_true():
    with patch('semantic_release.dist.config', {'upload_to_pypi': 'true', 'upload_to_release': 'true', 'build_command': 'make build'}):
        assert should_build() is True

def test_valid_input_only_pypi():
    with patch('semantic_release.dist.config', {'upload_to_pypi': 'true', 'upload_to_release': 'false', 'build_command': 'make build'}):
        assert should_build() is True
