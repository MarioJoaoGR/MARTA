
import pytest
from ansible.vars.manager import VariableManager

# Assuming some initialization of plugins and assignment to all_group
all_group = [lambda: print("Plugin 1 is playing."), lambda: print("Plugin 2 is playing."), lambda: print("Plugin 3 is playing.")]

def _plugins_play(groups):
    for group in groups:
        group()

@pytest.mark.parametrize("expected_output", [["Plugin 1 is playing.", "Plugin 2 is playing.", "Plugin 3 is playing."]])
def test_all_plugins_play(capsys, expected_output):
    _plugins_play([lambda: print("Plugin 1 is playing."), lambda: print("Plugin 2 is playing."), lambda: print("Plugin 3 is playing.")])
    captured = capsys.readouterr()
    assert captured.out == "\n".join(expected_output) + "\n"
