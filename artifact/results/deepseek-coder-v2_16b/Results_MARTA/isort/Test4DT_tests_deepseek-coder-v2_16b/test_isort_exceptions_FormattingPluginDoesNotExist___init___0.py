
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_formatting_plugin_does_not_exist():
    # Test that an exception is raised when a formatting plugin does not exist
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("non_existent_formatter")
    
    assert str(exc_info.value) == "Specified formatting plugin of non_existent_formatter does not exist. "
