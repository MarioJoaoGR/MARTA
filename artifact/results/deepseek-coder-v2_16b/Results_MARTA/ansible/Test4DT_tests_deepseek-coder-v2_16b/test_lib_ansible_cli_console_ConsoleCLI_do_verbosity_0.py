
import pytest
from ansible.cli.console import ConsoleCLI

def test_valid_input_verbosity():
    console = ConsoleCLI(args={'verbosity': '3'})
    assert console.do_verbosity('3') == None

