
import pytest
from httpie.output.formatters.json import JSONFormatter


def test_JSONFormatter_custom_enabled():
    formatter = JSONFormatter(format_options={'json': {'format': False}})
    assert not formatter.enabled, "Enabled should be False when format_options['json']['format'] is False"

def test_JSONFormatter_missing_format_option():
    with pytest.raises(KeyError):
        JSONFormatter()