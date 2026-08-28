
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

# Test for valid input scenario
def test_valid_input():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("my_formatter")
    assert str(exc_info.value) == "Specified formatting plugin of my_formatter does not exist. "

# Test for edge case scenario
def test_edge_case():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("another_formatter")
    assert str(exc_info.value) == "Specified formatting plugin of another_formatter does not exist. "

# Test for invalid input scenario
def test_invalid_input():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("non_existent_formatter")
    assert str(exc_info.value) == "Specified formatting plugin of non_existent_formatter does not exist. "
