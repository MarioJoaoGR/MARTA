
import pytest
from unittest.mock import patch, MagicMock
import ntpath
from ansible.plugins.shell.powershell import ShellModule

class TestShellModule:
    
    @classmethod
    def setup_class(cls):
        cls.shell_module = ShellModule()
    
    def test_join_path_basic(self):
        with patch('ansible.plugins.shell.powershell.ntpath') as mock_ntpath:
            mock_ntpath.normpath.return_value = 'c:\\windows\\system32'
            mock_ntpath.join.return_value = 'c:\\windows\\system32'
            
            result = self.shell_module.join_path('c:', 'windows', 'system32')
            assert result == 'c:\\windows\\system32'
    
    def test_join_path_mixed(self):
        with patch('ansible.plugins.shell.powershell.ntpath') as mock_ntpath:
            mock_ntpath.normpath.side_effect = lambda x: x.replace('/', '\\')
            mock_ntpath.join.return_value = 'c:\\windows\\system32'
            
            result = self.shell_module.join_path('c:/', 'windows', 'system32')
            assert result == 'c:\\windows\\system32'
    
    def test_join_path_absolute_relative(self):
        with patch('ansible.plugins.shell.powershell.ntpath') as mock_ntpath:
            mock_ntpath.normpath.side_effect = lambda x: x.replace('/', '\\')
            mock_ntpath.join.return_value = 'c:\\windows\\system32'
            
            result = self.shell_module.join_path('c:', '/windows/', '/system32/')
            assert result == 'c:\\windows\\system32'

if __name__ == '__main__':
    pytest.main()
