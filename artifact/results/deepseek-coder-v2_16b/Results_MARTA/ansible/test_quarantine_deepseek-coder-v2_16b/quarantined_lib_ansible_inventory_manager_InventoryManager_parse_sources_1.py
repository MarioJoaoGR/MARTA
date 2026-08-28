
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from unittest.mock import MagicMock, patch

# Test initialization without sources
def test_initialization_without_sources():
    loader = MagicMock()
    with pytest.raises(AnsibleError):
        manager = InventoryManager(loader=loader)
```

```python
# Test parsing sources successfully
def test_parse_sources():
    loader = MagicMock()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources)
    manager.parse_sources()
    assert len(manager._inventory.hosts) > 0
```

```python
# Test parsing sources without providing any sources should raise AnsibleError
def test_parse_sources_no_sources():
    loader = MagicMock()
    with pytest.raises(AnsibleError):
        manager = InventoryManager(loader=loader)
```

```python
# Test restricting to hosts successfully
def test_restrict_to_hosts():
    loader = MagicMock()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources)
    manager.parse_sources()
    manager.restrict_to_hosts(['host1', 'host2'])
    assert len(manager._restriction) > 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 12, col 1)
```
"""