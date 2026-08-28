
import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.arguments.option_helpers import add_runtask_options, maybe_unfrack_path



def test_invalid_inputs():
    parser = MagicMock()
    with patch('ansible.cli.arguments.option_helpers.maybe_unfrack_path', side_effect=ValueError):
        with pytest.raises(ValueError):
            add_runtask_options(parser)