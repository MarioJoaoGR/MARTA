
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_edge_case_none():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("my_formatter")
