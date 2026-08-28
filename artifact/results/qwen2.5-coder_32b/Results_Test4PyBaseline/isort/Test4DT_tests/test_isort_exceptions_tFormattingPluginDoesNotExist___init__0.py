
# Test case  
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_formatting_plugin_does_not_exist():
    # Test with a simple string
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist('markdown_formatter')
    assert str(excinfo.value) == "Specified formatting plugin of markdown_formatter does not exist. "
    assert excinfo.value.formatter == 'markdown_formatter'

def test_formatting_plugin_does_not_exist_with_empty_string():
    # Test with an empty string
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist('')
    assert str(excinfo.value) == "Specified formatting plugin of  does not exist. "
    assert excinfo.value.formatter == ''

def test_formatting_plugin_does_not_exist_with_whitespace():
    # Test with a string containing only whitespace
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist('   ')