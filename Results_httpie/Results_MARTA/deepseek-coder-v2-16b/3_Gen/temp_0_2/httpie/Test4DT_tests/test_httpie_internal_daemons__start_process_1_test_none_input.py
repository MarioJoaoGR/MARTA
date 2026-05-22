
import pytest
from subprocess import Popen, DEVNULL
from httpie.internal.daemons import _start_process
from unittest.mock import patch

def test_none_input():
    with pytest.raises(TypeError):
        with patch('httpie.internal.daemons._start_process'):
            _start_process(None)
