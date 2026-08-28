
import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector


def test_non_empty_input():
    # Create a temporary file to simulate /proc/cmdline with content
    temp_file_path = '/tmp/temp_cmdline'
    with open(temp_file_path, 'w') as f:
        f.write('BOOT_IMAGE=/vmlinuz-4.18.0-348.el8.0.2.x86_64 root=UUID=88997c35-9450-460f-9654-d86f8e1593b1 ro console=tty0 console=ttyS0,115200 quiet initcall_blacklist=algif_aead_init rd.driver.blacklist=nouveau rd.driver.blacklist=nova-core')
    
    collector = CmdLineFactCollector()
    cmdline_content = collector._get_proc_cmdline()
    assert isinstance(cmdline_content, str), "Expected a string"
    assert len(cmdline_content) > 0, "Expected non-empty string"