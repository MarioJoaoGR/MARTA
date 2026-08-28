
import pytest
from ansible.vars.manager import VarsWithSources

def test_getitem():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    with pytest.raises(KeyError):
        print(vars_with_sources['var3'])  # This should raise a KeyError

def test_getitem_debug():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    with pytest.raises(KeyError):
        print(vars_with_sources['var3'])  # This should raise a KeyError
    assert not hasattr(vars_with_sources, '_VarsWithSources__debug')  # Ensure debug is not set when accessing non-existent key

def test_getitem_source_tracking():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})