
import pytest
from ansible.plugins.connection.psrp import Connection
import os
import base64

@pytest.fixture(scope="module")
def valid_connection():
    return Connection(remote_addr='192.168.1.100', remote_user='admin', remote_password='password')

def test_valid_input(valid_connection):
    # Test successful file upload with valid inputs
    in_path = 'local_script.ps1'
    out_path = 'remote_path/on/host'
    rc, stdout, stderr, sha1_hash = valid_connection._put_file_old(in_path, out_path)
    
    assert rc == 0, f"Return code is not zero: {stderr}"
    assert os.path.exists(out_path), "File does not exist on remote host"
    calculated_sha1 = sha1()
    with open(in_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            calculated_sha1.update(chunk)
    assert sha1_hash == calculated_sha1.hexdigest(), "SHA1 hash does not match"

def test_edge_case():
    # Test edge cases such as empty strings or non-existent files
    conn = Connection(remote_addr='192.168.1.100', remote_user='admin', remote_password='password')
    
    in_path = ''
    out_path = 'non_existent_remote_path'
    with pytest.raises(AnsibleFileNotFound):
        conn._put_file_old(in_path, out_path)

def test_invalid_input():
    # Test error handling for invalid inputs like missing arguments
    conn = Connection()
    
    in_path = 'local_script.ps1'
    out_path = ''
    with pytest.raises(TypeError):
        conn._put_file_old(in_path, out_path)
