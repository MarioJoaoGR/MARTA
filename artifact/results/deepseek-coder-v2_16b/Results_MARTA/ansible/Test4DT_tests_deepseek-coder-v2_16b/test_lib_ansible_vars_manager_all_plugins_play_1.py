
import pytest
from unittest.mock import patch

# Assuming some initialization of plugins and assignment to all_group
all_group = [lambda: print("Plugin 1 is playing."), lambda: print("Plugin 2 is playing."), lambda: print("Plugin 3 is playing.")]

def test_valid_case():
    with patch('builtins.print') as mock_print:
        all_plugins_play()
        assert mock_print.call_count == len(all_group)
        for plugin in all_group:
            mock_print.assert_any_call(plugin.__name__)

def test_edge_case():
    with patch('builtins.print') as mock_print:
        all_group = []
        all_plugins_play()
        assert mock_print.call_count == 0

def test_error_case():
    with pytest.raises(NameError):
        all_plugins_play()
