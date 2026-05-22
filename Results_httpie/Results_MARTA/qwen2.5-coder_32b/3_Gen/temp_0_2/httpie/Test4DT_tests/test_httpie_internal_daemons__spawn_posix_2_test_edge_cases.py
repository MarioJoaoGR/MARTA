
import os
import sys
import platform
from contextlib import suppress
from typing import List
from httpie.core import main as httpie_main
from unittest.mock import patch
from httpie.internal.daemons import ProcessContext, _spawn_posix

def test_httpie_internal_daemons__spawn_posix_2_test_edge_cases():
    args = ['arg1', 'arg2']
    process_context = {'VAR': 'value'}
    
    with patch('os.fork', return_value=0):
        with patch('os.setsid'):
            with patch('httpie.core.main', autospec=True) as mock_main:
                _spawn_posix(args, process_context)
                
                if platform.system() != 'Darwin':
                    assert os.fork.call_count == 2
                    assert os.setsid.called
                    assert sys.stdin.closed
                    assert sys.stdout.closed
                    assert sys.stderr.closed
                else:
                    mock_main.assert_called_once_with(['http'] + args)
