
import pytest
from thefuck.types import Command, EmptyCommand
from unittest.mock import patch

def test_edge_case():
    with pytest.raises(EmptyCommand):
        Command.from_raw_script([''])
