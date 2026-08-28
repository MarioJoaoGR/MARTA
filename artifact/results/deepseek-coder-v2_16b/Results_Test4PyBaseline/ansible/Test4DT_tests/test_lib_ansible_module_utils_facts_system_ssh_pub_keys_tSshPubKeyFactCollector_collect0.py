# Module: ansible.module_utils.facts.system.ssh_pub_keys
import pytest
from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector

# Create an instance of SshPubKeyFactCollector
@pytest.fixture
def collector():
    return SshPubKeyFactCollector()

# Test case to check if the collect method returns a dictionary with SSH public key facts for all supported algorithms
def test_collect_returns_dict_with_ssh_public_key_facts(collector):
    facts = collector.collect()
    assert isinstance(facts, dict), "Expected a dictionary but got something else"
    expected_keys = {'ssh_host_key_dsa_public', 'ssh_host_key_rsa_public', 
                     'ssh_host_key_ecdsa_public', 'ssh_host_key_ed25519_public'}
    assert set(facts.keys()) == expected_keys, f"Expected keys {expected_keys} but got {set(facts.keys())}"

# Test case to check if the collect method returns an empty dictionary when no SSH public keys are found
def test_collect_returns_empty_dict_when_no_keys_found(mocker):
    mocker.patch('ansible.module_utils.facts.system.ssh_pub_keys.get_file_content', return_value=None)
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict), "Expected a dictionary but got something else"
    assert len(facts) == 0, "Expected an empty dictionary when no keys are found"

# Test case to check if the collect method returns a dictionary with SSH public key facts for all supported algorithms even if some files exist and others do not
def test_collect_returns_dict_with_ssh_public_key_facts_some_files_exist(mocker):
    # Mock get_file_content to return valid data for dsa and rsa, and None for ecdsa and ed25519
    mocker.patch('ansible.module_utils.facts.system.ssh_pub_keys.get_file_content', side_effect=['valid_dsa_data', 'valid_rsa_data', None, None])
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict), "Expected a dictionary but got something else"
    expected_keys = {'ssh_host_key_dsa_public', 'ssh_host_key_rsa_public'}
    assert set(facts.keys()) == expected_keys, f"Expected keys {expected_keys} but got {set(facts.keys())}"
