
import pytest
from unittest.mock import patch
from argparse import Namespace, ArgumentParser
from py_backwards.main import main
import sys



def test_invalid_inputs():
    with patch('argparse._sys.argv', ['py-backwards', '-i', 'dir1', 'dir2', '-o', '', '-t', '3.6']):
        args = Namespace(input=['dir1', 'dir2'], output=None, target='3.6', root=None, debug=False)
        assert main() == 1