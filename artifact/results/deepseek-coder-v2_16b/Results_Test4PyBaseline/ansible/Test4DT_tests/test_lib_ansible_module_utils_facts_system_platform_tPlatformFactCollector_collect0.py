# Module: ansible.module_utils.facts.system.platform
import pytest
import platform
import socket
import mock

class PlatformFactCollector:
    name = 'platform'
    _fact_ids = set(['system', 'kernel', 'kernel_version', 'machine',
        'python_version', 'architecture', 'machine_id'])
    
    def collect(self, module=None, collected_facts=None):
        platform_facts = {}
        # Collect system information using Python's built-in modules
        platform_facts['system'] = platform.system()
        platform_facts['kernel'] = platform.release()
        platform_facts['kernel_version'] = platform.version()
        platform_facts['machine'] = platform.machine()
        platform_facts['python_version'] = platform.python_version()
        platform_facts['fqdn'] = socket.getfqdn()
        platform_facts['hostname'] = platform.node().split('.')[0]
        platform_facts['nodename'] = platform.node()
        platform_facts['domain'] = '.'.join(platform_facts['fqdn'].split('.')[1:])
        arch_bits = platform.architecture()[0]
        platform_facts['userspace_bits'] = arch_bits.replace('bit', '')
        
        # Additional logic to determine architecture based on machine type and userspace bits
        if platform_facts['machine'] == 'x86_64':
            platform_facts['architecture'] = platform_facts['machine']
            if platform_facts['userspace_bits'] == '64':
                platform_facts['userspace_architecture'] = 'x86_64'
            elif platform_facts['userspace_bits'] == '32':
                platform_facts['userspace_architecture'] = 'i386'
        elif solaris_i86_re.search(platform_facts['machine']):
            platform_facts['architecture'] = 'i386'
            if platform_facts['userspace_bits'] == '64':
                platform_facts['userspace_architecture'] = 'x86_64'
            elif platform_facts['userspace_bits'] == '32':
                platform_facts['userspace_architecture'] = 'i386'
        else:
            platform_facts['architecture'] = platform_facts['machine']
        
        if platform_facts['system'] == 'AIX':
            getconf_bin = module.get_bin_path('getconf')
            if getconf_bin:
                rc, out, err = module.run_command([getconf_bin, 'MACHINE_ARCHITECTURE'])
                data = out.splitlines()
                platform_facts['architecture'] = data[0]
            else:
                bootinfo_bin = module.get_bin_path('bootinfo')
                rc, out, err = module.run_command([bootinfo_bin, '-p'])
                data = out.splitlines()
                platform_facts['architecture'] = data[0]
        elif platform_facts['system'] == 'OpenBSD':
            platform_facts['architecture'] = platform.uname()[5]
        
        machine_id = get_file_content("/var/lib/dbus/machine-id") or get_file_content("/etc/machine-id")
        if machine_id:
            machine_id = machine_id.splitlines()[0]
            platform_facts["machine_id"] = machine_id
        
        return platform_facts

# Mock functions for testing
class CustomModule:
    def get_bin_path(self, bin_name):
        return '/usr/bin/getconf' if bin_name == 'getconf' else None

    def run_command(self, command):
        if command[0] == '/usr/bin/getconf':
            return 0, "x86_64\n", ""
        elif command[0] == '/usr/bin/bootinfo':
            return 0, "i386\n", ""
        return -1, "", "Command not found"

# Test cases for PlatformFactCollector class
def test_collect_default():
    collector = PlatformFactCollector()
    facts = collector.collect()
    assert 'system' in facts
    assert 'kernel' in facts
    assert 'kernel_version' in facts
    assert 'machine' in facts
    assert 'python_version' in facts
    assert 'architecture' in facts
    assert 'machine_id' in facts

def test_collect_with_custom_module():
    custom_module = CustomModule()
    collector = PlatformFactCollector()
    facts = collector.collect(module=custom_module)
    assert 'system' in facts
    assert 'kernel' in facts
    assert 'kernel_version' in facts
    assert 'machine' in facts
    assert 'python_version' in facts
    assert 'architecture' in facts
    assert 'machine_id' in facts

def test_collect_in_program():
    collector = PlatformFactCollector()
    facts = collector.collect()
    assert 'system' in facts
    assert 'kernel' in facts
    assert 'kernel_version' in facts
    assert 'machine' in facts
    assert 'python_version' in facts
    assert 'architecture' in facts
    assert 'machine_id' in facts
