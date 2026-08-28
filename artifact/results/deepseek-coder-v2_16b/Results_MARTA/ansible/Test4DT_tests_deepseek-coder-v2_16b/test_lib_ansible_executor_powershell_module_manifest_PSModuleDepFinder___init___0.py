
import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

# Test for valid input script content parsing

# Test for edge case where script content is empty
def test_edge_case():
    finder = PSModuleDepFinder()
    script_content = ""
    with pytest.raises(AttributeError):
        finder._parse_scripts(script_content)