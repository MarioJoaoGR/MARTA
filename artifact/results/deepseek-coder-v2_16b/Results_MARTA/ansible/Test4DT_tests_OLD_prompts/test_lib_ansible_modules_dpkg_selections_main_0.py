
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.dpkg_selections import main
from ansible.module_utils.basic import AnsibleModule



def test_invalid_selection():
    with patch('ansible.modules.dpkg_selections.AnsibleModule') as mock_module:
        mock_module.return_value = MagicMock()
        mock_module.return_value.params = {'name': 'example_package', 'selection': 'invalid_choice'}
        mock_module.return_value.get_bin_path.return_value = '/usr/bin/dpkg'

        with pytest.raises(ValueError):
            main()