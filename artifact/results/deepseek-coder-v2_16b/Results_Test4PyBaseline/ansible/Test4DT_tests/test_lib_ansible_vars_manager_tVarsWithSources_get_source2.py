
import pytest
from ansible.vars.manager import VarsWithSources

# Test getting a source for a non-existent key
def test_get_source_non_existent_key():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources.get_source('var3') is None
