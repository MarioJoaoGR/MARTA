
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.utils import LazyChoices

def test_invalid_input():
    with patch('httpie.cli.utils.LazyChoices.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            lazy_choices = LazyChoices(getter=lambda: [1, 2, 3], help_formatter='invalid_formatter')
