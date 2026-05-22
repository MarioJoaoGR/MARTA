
import unittest
from httpie.plugins.manager import PluginManager
from unittest.mock import patch, MagicMock
from typing import Dict, List, Type
from itertools import groupby
from operator import attrgetter

class TestPluginManager(unittest.TestCase):
    
    @patch('httpie.plugins.manager.PluginManager.get_formatters', return_value=[
        MagicMock(group_name='html'),
        MagicMock(group_name='csv'),
        MagicMock(group_name='json')
    ])
    def test_get_formatters_grouped(self, mock_get_formatters):
        manager = PluginManager()
        grouped_formatters = manager.get_formatters_grouped()
        
        self.assertIsInstance(grouped_formatters, dict)
        self.assertEqual(len(grouped_formatters), 3)
        for group in grouped_formatters.values():
            self.assertIsInstance(group, list)
            for formatter in group:
                self.assertIsInstance(formatter, MagicMock)
        
        # Additional assertions to check the content of the groups
        html_group = grouped_formatters['html']
        csv_group = grouped_formatters['csv']
        json_group = grouped_formatters['json']
        
        self.assertEqual(len(html_group), 1)
        self.assertEqual(len(csv_group), 1)
        self.assertEqual(len(json_group), 1)
        
        # Check if the mocked get_formatters was called
        mock_get_formatters.assert_called_once()

if __name__ == '__main__':
    unittest.main()
