
import pytest
from thefuck.types import CorrectedCommand

# Test initialization with a custom side effect function and default priority
def test_correctedcommand_initialization_with_custom_side_effect():
    def side_effect_function(command, message):
        assert command.script == "ls"