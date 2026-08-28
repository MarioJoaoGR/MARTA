
import pytest
from pathlib import Path
import sys
from thefuck.corrector import get_rules_import_paths
from unittest.mock import patch

# Mock settings and sys for testing
@patch('thefuck.corrector.settings', new={'user_dir': Path('/user/rules')})
@patch('thefuck.corrector.sys', new={'path': ['/system/paths']})
def test_get_rules_import_paths():
    # Test bundled rules path
    with patch('thefuck.corrector.__file__', return_value='/module/path'):
        expected_bundled = Path('/module/path').parent / 'rules'