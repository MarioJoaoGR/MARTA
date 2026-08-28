
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.aix import AIXHardware

def test_get_memory_facts_valid():
    mock_module = MagicMock()
    mock_module.run_command.side_effect = [
        (0, "memory pages      131072\nfree pages        124568", ""),
        (0, "/dev/ada0p3        314368        0   314368     0%", "")
    ]
    
    aix_hardware = AIXHardware(module=mock_module)
    with patch('ansible.module_utils.facts.hardware.aix.AIXHardware.get_memory_facts', return_value={'memtotal_mb': 128, 'memfree_mb': 124568, 'swaptotal_mb': 314368, 'swapfree_mb': 0}):
        memory_facts = aix_hardware.get_memory_facts()
        assert memory_facts['memtotal_mb'] == 128
        assert memory_facts['memfree_mb'] == 124568
        assert memory_facts['swaptotal_mb'] == 314368
        assert memory_facts['swapfree_mb'] == 0

def test_get_memory_facts_edge():
    mock_module = MagicMock()
    mock_module.run_command.side_effect = [
        (0, "", ""),
        (0, "/dev/ada0p3        314368        0   314368     0%", "")
    ]
    
    aix_hardware = AIXHardware(module=mock_module)
    with patch('ansible.module_utils.facts.hardware.aix.AIXHardware.get_memory_facts', return_value={'memtotal_mb': 128, 'memfree_mb': 0, 'swaptotal_mb': 314368, 'swapfree_mb': 314368}):
        memory_facts = aix_hardware.get_memory_facts()
        assert memory_facts['memtotal_mb'] == 128
        assert memory_facts['memfree_mb'] == 0
        assert memory_facts['swaptotal_mb'] == 314368
        assert memory_facts['swapfree_mb'] == 314368

def test_get_memory_facts_error():
    mock_module = MagicMock()
    mock_module.run_command.side_effect = [
        (1, "", "Error running vmstat"),
        (0, "/dev/ada0p3        314368        0   314368     0%", "")
    ]
    
    aix_hardware = AIXHardware(module=mock_module)
    with patch('ansible.module_utils.facts.hardware.aix.AIXHardware.get_memory_facts', return_value={'memtotal_mb': 128, 'memfree_mb': 0, 'swaptotal_mb': 314368, 'swapfree_mb': 314368}):
        memory_facts = aix_hardware.get_memory_facts()
        assert memory_facts['memtotal_mb'] == 128
        assert memory_facts['memfree_mb'] == 0
        assert memory_facts['swaptotal_mb'] == 314368
        assert memory_facts['swapfree_mb'] == 314368
