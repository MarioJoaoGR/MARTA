
import pytest
from unittest.mock import MagicMock

# Import the function from the specified module
from ansible.modules.apt_repository import install_python_apt

@pytest.fixture
def mock_module():
    # Create a mock Ansible module object
    module = MagicMock()
    return module

def test_install_python_apt_normal(mock_module):
    """Test the function with a normal package installation."""
    apt_pkg_name = 'python3-pip'
    mock_module.check_mode = False
    mock_module.get_bin_path.return_value = '/usr/bin/apt-get'
    
    # Mocking the run_command method to return successful results for apt-get update and install
    mock_module.run_command.side_effect = [
        (0, "Updated", ""),  # Successfully updated package list
        (0, "Installed", "")  # Successfully installed the package
    ]
    
    install_python_apt(mock_module, apt_pkg_name)
    
    mock_module.run_command.assert_called_with(['/usr/bin/apt-get', 'install', apt_pkg_name, '-y', '-q'])
    assert not mock_module.fail_json.called

def test_install_python_apt_check_mode(mock_module):
    """Test the function in check mode."""
    apt_pkg_name = 'python3-pip'
    mock_module.check_mode = True
    
    with pytest.raises(SystemExit) as e:
        install_python_apt(mock_module, apt_pkg_name)
        
    assert str(e.value) == "Module failed: %s must be installed to use check mode" % apt_pkg_name
    mock_module.fail_json.assert_called_with(msg="Module failed: %s must be installed to use check mode" % apt_pkg_name)

def test_install_python_apt_update_failure(mock_module):
    """Test the function when apt-get update fails."""
    apt_pkg_name = 'python3-pip'
    mock_module.check_mode = False
    mock_module.get_bin_path.return_value = '/usr/bin/apt-get'
    
    # Mocking the run_command method to return a failure result for apt-get update
    mock_module.run_command.side_effect = [(1, "", "Update failed")]
    
    with pytest.raises(SystemExit) as e:
        install_python_apt(mock_module, apt_pkg_name)
        
    assert str(e.value) == "Module failed: Failed to auto-install %s. Error was: '%s'" % (apt_pkg_name, "Update failed")
    mock_module.fail_json.assert_called_with(msg="Failed to auto-install %s. Error was: '%s'" % (apt_pkg_name, "Update failed"))

def test_install_python_apt_install_failure(mock_module):
    """Test the function when apt-get install fails."""
    apt_pkg_name = 'python3-pip'
    mock_module.check_mode = False
    mock_module.get_bin_path.return_value = '/usr/bin/apt-get'
    
    # Mocking the run_command method to return a failure result for apt-get install
    mock_module.run_command.side_effect = [(0, "Updated", ""), (1, "", "Install failed")]
    
    with pytest.raises(SystemExit) as e:
        install_python_apt(mock_module, apt_pkg_name)
        
    assert str(e.value) == "Module failed: Failed to auto-install %s. Error was: '%s'" % (apt_pkg_name, "Install failed")
    mock_module.fail_json.assert_called_with(msg="Failed to auto-install %s. Error was: '%s'" % (apt_pkg_name, "Install failed"))
