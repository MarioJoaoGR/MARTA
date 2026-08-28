
import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError

# Test 1: Valid input with loader specified
def test_valid_input_with_loader():
    # Arrange
    class BaseClass: pass
    class LoaderMock: pass
    
    base = BaseClass()
    loader = LoaderMock()
    conditional = Conditional(loader=loader)
    
    # Act and Assert
    assert hasattr(conditional, '_loader')
    assert conditional._loader == loader

# Test 2: Missing loader raises AnsibleError
def test_missing_loader():
    # Arrange
    class BaseClass: pass
    
    base = BaseClass()
    with pytest.raises(AnsibleError):
        Conditional()

# Test 3: Invalid conditional string handling
def test_invalid_conditional():
    # Arrange
    class BaseClass: pass
    class LoaderMock: pass
    class TemplarMock:
        def is_template(self, s): return "{{ }}" in s
        def template(self, s, disable_lookups=False): return s.replace("{{ }}", "")
    
    base = BaseClass()
    loader = LoaderMock()
    templar = TemplarMock()
    conditional = Conditional(loader=loader)
    conditional._when = ["{{ invalid_jinja2 }}"]
    
    # Act and Assert
    with pytest.raises(AnsibleError):
        conditional._check_conditional("{{ invalid_jinja2 }}", templar, {})
