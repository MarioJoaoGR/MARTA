# Module: ansible.module_utils.facts.utils
import os
from ansible.module_utils.facts.utils import get_mount_size

def test_get_mount_size_root():
    root_mount_info = get_mount_size('/')
    assert isinstance(root_mount_info, dict), "Expected a dictionary"
    assert 'size_total' in root_mount_info, "Expected 'size_total' key"
    assert 'size_available' in root_mount_info, "Expected 'size_available' key"
    assert 'block_size' in root_mount_info, "Expected 'block_size' key"
    assert 'block_total' in root_mount_info, "Expected 'block_total' key"
    assert 'block_available' in root_mount_info, "Expected 'block_available' key"
    assert 'block_used' in root_mount_info, "Expected 'block_used' key"
    assert 'inode_total' in root_mount_info, "Expected 'inode_total' key"
    assert 'inode_available' in root_mount_info, "Expected 'inode_available' key"
    assert 'inode_used' in root_mount_info, "Expected 'inode_used' key"

def test_get_mount_size_home():
    home_mount_info = get_mount_size('/home')
    assert isinstance(home_mount_info, dict), "Expected a dictionary"
    assert 'size_total' in home_mount_info, "Expected 'size_total' key"
    assert 'size_available' in home_mount_info, "Expected 'size_available' key"
    assert 'block_size' in home_mount_info, "Expected 'block_size' key"
    assert 'block_total' in home_mount_info, "Expected 'block_total' key"
    assert 'block_available' in home_mount_info, "Expected 'block_available' key"
    assert 'block_used' in home_mount_info, "Expected 'block_used' key"
    assert 'inode_total' in home_mount_info, "Expected 'inode_total' key"
    assert 'inode_available' in home_mount_info, "Expected 'inode_available' key"
    assert 'inode_used' in home_mount_info, "Expected 'inode_used' key"

def test_get_mount_size_custom():
    custom_mount_info = get_mount_size('/data')
    assert isinstance(custom_mount_info, dict), "Expected a dictionary"
    assert 'size_total' in custom_mount_info, "Expected 'size_total' key"
    assert 'size_available' in custom_mount_info, "Expected 'size_available' key"
    assert 'block_size' in custom_mount_info, "Expected 'block_size' key"
    assert 'block_total' in custom_mount_info, "Expected 'block_total' key"
    assert 'block_available' in custom_mount_info, "Expected 'block_available' key"
    assert 'block_used' in custom_mount_info, "Expected 'block_used' key"
    assert 'inode_total' in custom_mount_info, "Expected 'inode_total' key"
    assert 'inode_available' in custom_mount_info, "Expected 'inode_available' key"
    assert 'inode_used' in custom_mount_info, "Expected 'inode_used' key"
