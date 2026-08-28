
import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetwork

# Assuming 'self' is an instance of HPUXNetwork with appropriate module setup
def test_get_default_interfaces():
    # Create a mock instance of HPUXNetwork for testing
    class MockModule:
        def run_command(self, command):
            if command == "/usr/bin/netstat -nr":
                return (0, "default      192.168.1.1 192.168.1.254 UG    0      0 eth0\nother   192.168.1.2 192.168.1.254 UG    0      0 eth1\n", "")
            else:
                raise ValueError("Unknown command")

    mock_module = MockModule()
    hpux_network = HPUXNetwork(module=mock_module)  # Corrected the constructor call for HPUXNetwork

    # Call the function and check the result
    result = hpux_network.get_default_interfaces()
    assert 'default_interface' in result
    assert 'default_gateway' in result