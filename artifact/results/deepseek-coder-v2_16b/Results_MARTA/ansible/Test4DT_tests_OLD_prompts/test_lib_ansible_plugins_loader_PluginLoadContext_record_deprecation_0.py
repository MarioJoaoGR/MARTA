
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import PluginLoadContext

def test_record_deprecation():
    context = PluginLoadContext()
    with patch('ansible.plugins.loader.display') as mock_display:
        mock_display.deprecated = MagicMock()
        deprecation_info = {'warning_text': 'Use new_plugin instead.', 'removal_date': '2023-12-31'}
        context.record_deprecation('old_plugin', deprecation_info, 'my_collection')
        assert context.deprecated is True
        mock_display.deprecated.assert_called_with(
            'old_plugin has been deprecated. Use new_plugin instead.', 
            date='2023-12-31', 
            version=None, 
            collection_name='my_collection'
        )
