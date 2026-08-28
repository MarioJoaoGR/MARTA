
import os
import pytest
from unittest.mock import patch

def get_mount_size(mountpoint):
    mount_size = {}

    try:
        statvfs_result = os.statvfs(mountpoint)
        mount_size['size_total'] = statvfs_result.f_frsize * statvfs_result.f_blocks
        mount_size['size_available'] = statvfs_result.f_frsize * (statvfs_result.f_bavail)

        # Block total/available/used
        mount_size['block_size'] = statvfs_result.f_bsize
        mount_size['block_total'] = statvfs_result.f_blocks
        mount_size['block_available'] = statvfs_result.f_bavail
        mount_size['block_used'] = mount_size['block_total'] - mount_size['block_available']

        # Inode total/available/used
        mount_size['inode_total'] = statvfs_result.f_files
        mount_size['inode_available'] = statvfs_result.f_favail
        mount_size['inode_used'] = mount_size['inode_total'] - mount_size['inode_available']
    except OSError:
        pass

    return mount_size

# Test scenarios
def test_valid_case():
    with patch('os.statvfs', return_value=type('statvfs', (object,), {'f_frsize': 1024, 'f_blocks': 1000, 'f_bavail': 900, 'f_bsize': 1024, 'f_files': 5000, 'f_favail': 4500})()):
        result = get_mount_size("/")
        assert result == {
            'size_total': 1024 * 1000,
            'size_available': 1024 * 900,
            'block_size': 1024,
            'block_total': 1000,
            'block_available': 900,
            'block_used': 100,
            'inode_total': 5000,
            'inode_available': 4500,
            'inode_used': 500
        }

def test_edge_case():
    with patch('os.statvfs', side_effect=OSError(2, "No such file or directory")):
        result = get_mount_size(None)
        assert result == {}

def test_error_case():
    with pytest.raises(TypeError):
        get_mount_size("invalid_mountpoint")
