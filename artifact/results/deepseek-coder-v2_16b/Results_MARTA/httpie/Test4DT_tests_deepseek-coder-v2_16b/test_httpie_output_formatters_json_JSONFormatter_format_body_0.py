
import pytest
from httpie.output.formatters.json import JSONFormatter


def test_custom_initialization_with_format_true():
    formatter = JSONFormatter(format_options={'json': {'format': True}})
    assert formatter.enabled is True, "When format_options['json']['format'] is True, enabled should be True"

def test_custom_initialization_with_format_false():
    formatter = JSONFormatter(format_options={'json': {'format': False}})
    assert not formatter.enabled, "When format_options['json']['format'] is False, enabled should be False"

