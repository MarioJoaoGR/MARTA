
import pytest
from unittest.mock import patch, MagicMock
from flutils.pathutils import get_os_group
import grp
import pwd


def test_with_group_name():
    with patch('grp.getgrnam') as mock_getgrnam:
        mock_getgrnam.return_value = MagicMock(spec=grp.struct_group)
        group = get_os_group('test_group')
        assert group == mock_getgrnam.return_value

def test_with_group_id():
    with patch('grp.getgrgid') as mock_getgrgid:
        mock_getgrgid.return_value = MagicMock(spec=grp.struct_group)
        group = get_os_group(2001)
        assert group == mock_getgrgid.return_value