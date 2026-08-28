# Module: ansible.module_utils.facts.network.fc_wwn
import pytest
from your_module import FcWwnInitiatorFactCollector
import sys
import glob

# Assuming get_file_lines is defined elsewhere in your codebase
def get_file_lines(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

class MockModule:
    def __init__(self):
        self.bin_paths = {
            'fcinfo': '/usr/local/bin/fcinfo',
            'ioscan': '/usr/local/bin/ioscan',
            'lscfg': '/usr/local/bin/lscfg',
            'fcmsutil': '/opt/puppetlabs/bin/fcmsutil'
        }
    
    def get_bin_path(self, command):
        return self.bin_paths.get(command)
    
    def run_command(self, command):
        # Mock the output for fcinfo and ioscan commands
        if command == 'fcinfo hba-port':
            return 0, "HBA Port WWN: 10000090fa1658de\n", ""
        elif command == '/usr/local/bin/ioscan -fnC FC':
            return 0, "/dev/fcd0 /dev/fcd1\n", ""
        else:
            raise ValueError(f"Unknown command: {command}")

class MockSys:
    def __init__(self):
        self.platform = None
    
    def startswith(self, prefix):
        if prefix == 'linux':
            self.platform = 'linux'
            return True
        elif prefix == 'sunos':
            self.platform = 'sunos'
            return True
        elif prefix == 'aix':
            self.platform = 'aix'
            return True
        elif prefix == 'hp-ux':
            self.platform = 'hp-ux'
            return True
        return False

# Mock the sys module
sys.platform = MockSys()

@pytest.fixture
def collector():
    return FcWwnInitiatorFactCollector()

@pytest.fixture
def collected_facts():
    return {}

@pytest.mark.skipif(not sys.platform.startswith('linux'), reason="Linux specific test")
def test_collect_on_linux(collector, collected_facts):
    # Mock the glob module to simulate Linux filesystem
    with pytest.MonkeyPatch.context() as mp_mock:
        mp_mock.setattr(glob, 'glob', lambda pattern: ['/sys/class/fc_host/1/port_name'])
        mp_mock.setattr('/sys/class/fc_host/1/port_name', "0x21000014ff52a9bb\n")
        
        result = collector.collect(collected_facts=collected_facts)
        assert 'fibre_channel_wwn' in result
        assert len(result['fibre_channel_wwn']) == 1
        assert result['fibre_channel_wwn'][0] == '21000014ff52a9bb'

@pytest.mark.skipif(not sys.platform.startswith('sunos'), reason="SunOS specific test")
def test_collect_on_sunos(collector, collected_facts):
    # Create a mock module instance for SunOS
    module = MockModule()
    
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert 'fibre_channel_wwn' in result
    assert len(result['fibre_channel_wwn']) == 1
    assert result['fibre_channel_wwn'][0] == '10000090fa1658de'

@pytest.mark.skipif(not sys.platform.startswith('aix'), reason="AIX specific test")
def test_collect_on_aix(collector, collected_facts):
    # Create a mock module instance for AIX
    module = MockModule()
    
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert 'fibre_channel_wwn' in result
    assert len(result['fibre_channel_wwn']) == 1
    assert result['fibre_channel_wwn'][0] == '10000090fa551509'

@pytest.mark.skipif(not sys.platform.startswith('hp-ux'), reason="HP-UX specific test")
def test_collect_on_hpux(collector, collected_facts):
    # Create a mock module instance for HP-UX
    module = MockModule()
    
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert 'fibre_channel_wwn' in result
    assert len(result['fibre_channel_wwn']) == 1
    assert result['fibre_channel_wwn'][0] == '50060b00006975ec'

@pytest.mark.parametrize("platform, expected", [
    ('linux', ['21000014ff52a9bb']),
    ('sunos', ['10000090fa1658de']),
    ('aix', ['10000090fa551509']),
    ('hp-ux', ['50060b00006975ec'])
])
def test_collect_generic(collector, collected_facts, platform, expected):
    # Mock the sys module to simulate different platforms
    with pytest.MonkeyPatch.context() as mp_mock:
        mp_mock.setattr(sys, 'platform', platform)
        
        result = collector.collect(collected_facts=collected_facts)
        assert 'fibre_channel_wwn' in result
        assert len(result['fibre_channel_wwn']) == 1
        assert result['fibre_channel_wwn'][0] == expected[0]
