
import pytest
from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector

# Create an instance of SshPubKeyFactCollector
@pytest.fixture
def collector():
    return SshPubKeyFactCollector()

# Test case to check if the collect method initializes ssh_pub_key_facts correctly
def test_collect_initializes_ssh_pub_key_facts(collector):
    facts = collector.collect()
    assert isinstance(facts, dict), "Expected a dictionary but got something else"
    expected_keys = {'ssh_host_key_dsa_public', 'ssh_host_key_rsa_public', 
                     'ssh_host_key_ecdsa_public', 'ssh_host_key_ed25519_public'}