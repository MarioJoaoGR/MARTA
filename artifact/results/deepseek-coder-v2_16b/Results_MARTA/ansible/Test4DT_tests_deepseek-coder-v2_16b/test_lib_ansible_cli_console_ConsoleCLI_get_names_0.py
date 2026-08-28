
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI
import cmd





def test_edge_case_list_empty():
    args = {}
    with pytest.raises(ValueError):
        cli = ConsoleCLI(args)