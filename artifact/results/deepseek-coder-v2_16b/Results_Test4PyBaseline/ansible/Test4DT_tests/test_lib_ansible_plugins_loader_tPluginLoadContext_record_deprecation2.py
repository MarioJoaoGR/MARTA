
import pytest
from ansible.plugins.loader import PluginLoadContext
from datetime import datetime

# Test case for handling no deprecation details provided
def test_record_deprecation_no_deprecation():
    load_context = PluginLoadContext()
    result = load_context.record_deprecation("test_feature", {}, "test_collection")
    assert result == load_context

# Test case for handling deprecation with only warning text provided
def test_record_deprecation_with_warning_text():
    load_context = PluginLoadContext()
    deprecation = {'warning_text': 'This feature is deprecated.'}
    result = load_context.record_deprecation("test_feature", deprecation, "test_collection")
    assert load_context.deprecated is True
    assert load_context.removal_date is None
    assert len(load_context.deprecation_warnings) == 1