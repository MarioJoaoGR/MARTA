
import pytest
from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector

# Fixture to create an instance of SshPubKeyFactCollector for tests
@pytest.fixture(scope="function")
def ssh_pub_key_collector():
    return SshPubKeyFactCollector()

# Test scenario 1: test valid input with real directories and keys
def test_valid_input(ssh_pub_key_collector, tmpdir):
    # Create fake SSH key files in a temporary directory
    for algo in ('dsa', 'rsa', 'ecdsa', 'ed25519'):
        file_path = tmpdir.join(f"ssh_host_{algo}_key.pub")
        file_path.write(f"{algo} public key content")
    
    # Call the collect method
    collected_facts = ssh_pub_key_collector.collect()
    
    # Assert that the collected facts contain the expected keys and types
    assert 'ssh_host_key_dsa_public' in collected_facts
    assert 'ssh_host_key_rsa_public' in collected_facts
    assert 'ssh_host_key_ecdsa_public' in collected_facts
    assert 'ssh_host_key_ed25519_public' in collected_facts
    assert collected_facts['ssh_host_key_dsa_public'] == "dsa public key content"
    assert collected_facts['ssh_host_key_rsa_public'] == "rsa public key content"
    assert collected_facts['ssh_host_key_ecdsa_public'] == "ecdsa public key content"
    assert collected_facts['ssh_host_key_ed25519_public'] == "ed25519 public key content"
    assert collected_facts['ssh_host_key_dsa_public_keytype'] == 'dsa'
    assert collected_facts['ssh_host_key_rsa_public_keytype'] == 'rsa'
    assert collected_facts['ssh_host_key_ecdsa_public_keytype'] == 'ecdsa'
    assert collected_facts['ssh_host_key_ed25519_public_keytype'] == 'ed25519'

# Test scenario 2: test edge case where no SSH keys are present
def test_edge_case(ssh_pub_key_collector, tmpdir):
    # No SSH key files in the temporary directory
    
    # Call the collect method
    collected_facts = ssh_pub_key_collector.collect()
    
    # Assert that no keys are collected
    assert not collected_facts

# Test scenario 3: test invalid input handling, e.g., incorrect module type
def test_invalid_input():
    with pytest.raises(TypeError):
        SshPubKeyFactCollector().collect(module="invalid_type")
