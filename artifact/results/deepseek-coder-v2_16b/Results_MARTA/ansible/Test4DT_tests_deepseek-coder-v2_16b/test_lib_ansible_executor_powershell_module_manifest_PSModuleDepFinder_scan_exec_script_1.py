
import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

def test_scan_exec_script():
    finder = PSModuleDepFinder()
    name = "SomeScript"
    
    # Mock the data retrieval for a script
    with pytest.raises(Exception):
        finder.scan_exec_script(name)

    assert not finder.exec_scripts, "Expected exec_scripts to be empty after failing scan due to missing data."
