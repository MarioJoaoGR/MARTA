
import pytest
from httpie.output.formatters.json import JSONFormatter
import json

# Test initialization with default enabled setting
def test_init_default():
    formatter = JSONFormatter(format_options={'json': {'format': True}})
    assert formatter.enabled is True

# Test initialization with explicit JSON formatting enabled
def test_init_explicit_formatting():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'sort_keys': True, 'indent': 4}})
    assert formatter.enabled is True
    assert formatter.format_options['json']['sort_keys'] is True