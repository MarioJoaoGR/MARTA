
import pytest
from pathlib import Path
import sys
from unittest.mock import patch
from thefuck.corrector import get_rules_import_paths

# Mock settings for testing user directory
@patch('thefuck.corrector.settings', new={'user_dir': Path('/user/rules')})
def test_get_rules_import_paths():
    # Test bundled rules path
    with patch('thefuck.corrector.__file__', return_value='/module/path'):
        expected_bundled = Path('/module/path').parent / 'rules'