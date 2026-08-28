
import pytest

class FormattingPluginDoesNotExist(Exception):
    """
    Exception raised when a specified formatting plugin is not found.
    """
    def __init__(self, formatter: str):
        super().__init__(f"Specified formatting plugin of {formatter} does not exist. ")
        self.formatter = formatter

def test_valid_formatter_name():
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist('valid_plugin')
    assert str(excinfo.value) == "Specified formatting plugin of valid_plugin does not exist. "

def test_edge_case_none():
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist(None)
    assert str(excinfo.value) == "Specified formatting plugin of None does not exist. "

def test_invalid_formatter_name():
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist('')
    assert str(excinfo.value) == "Specified formatting plugin of  does not exist. "
    
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist('non_existent_plugin')
    assert str(excinfo.value) == "Specified formatting plugin of non_existent_plugin does not exist. "
