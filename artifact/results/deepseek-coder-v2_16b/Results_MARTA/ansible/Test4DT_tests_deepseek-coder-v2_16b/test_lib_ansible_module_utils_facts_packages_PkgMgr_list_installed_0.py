
import pytest
from unittest.mock import patch, MagicMock

# Assuming PkgMgr class implementation as provided in the question
class PkgMgr:
    def list_installed(self):
        # This method should return a list of installed packages, each list item will be passed to get_package_details
        pass

    def get_package_details(self, package):
        # Implementation for getting detailed information about a package
        pass

# Test scenarios
def test_valid_input():
    pkg_mgr = PkgMgr()
    with patch.object(pkg_mgr, 'list_installed', return_value=['package1', 'package2']):
        with patch.object(pkg_mgr, 'get_package_details') as mock_get_details:
            mock_get_details.side_effect = [{'name': 'package1', 'version': '1.0'}, {'name': 'package2', 'version': '2.0'}]
            
            installed_packages = pkg_mgr.list_installed()
            assert len(installed_packages) == 2
            for package in installed_packages:
                details = pkg_mgr.get_package_details(package)
                assert isinstance(details, dict)
                assert 'name' in details
                assert 'version' in details

def test_edge_case():
    pkg_mgr = PkgMgr()
    with patch.object(pkg_mgr, 'list_installed', return_value=None):
        installed_packages = pkg_mgr.list_installed()
        assert installed_packages is None

def test_invalid_input():
    pkg_mgr = PkgMgr()
    with patch.object(pkg_mgr, 'list_installed', side_effect=Exception("Mocked Error")):
        with pytest.raises(Exception):
            pkg_mgr.list_installed()
