
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_valid_input():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("my_formatter")
    assert str(exc_info.value) == "Specified formatting plugin of my_formatter does not exist. "
