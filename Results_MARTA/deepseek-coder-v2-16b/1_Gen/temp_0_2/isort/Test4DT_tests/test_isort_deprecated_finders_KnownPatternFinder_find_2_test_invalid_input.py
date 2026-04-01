
import pytest
from isort.deprecated.finders import KnownPatternFinder
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("module_name, expected", [
    ("os", "standard"),  # Valid module name should return the corresponding placement
    ("sys", "standard"),  # Another valid module name with standard library placement
    ("unknown", None),     # Invalid module name should return None
])
def test_invalid_input(module_name, expected):
    config = MagicMock()
    config.sections = ["standard"]
    config.known_standard = ["os", "sys"]
    finder = KnownPatternFinder(config)
    
    with patch('isort.deprecated.finders.re', autospec=True) as mock_re:
        # Mock re.compile to return a pattern that matches the module name
        mock_pattern = MagicMock()
        mock_pattern.match.return_value = True if expected else False
        mock_re.compile.return_value = mock_pattern
        
        assert finder.find(module_name) == expected
