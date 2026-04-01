
import sys
import os
from unittest.mock import MagicMock, patch
import pytest
from flutes.io import shut_up

def test_shut_up_context_manager():
    with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new=MagicMock()) as mock_stderr:
        # Capture the original file descriptors
        stdout_fd = sys.stdout.fileno()
        stderr_fd = sys.stderr.fileno()
    
        with shut_up(stderr=True):
            assert not mock_stderr.called
            assert not mock_stdout.called

def test_shut_up_decorator():
    with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new=MagicMock()) as mock_stderr:
        # Original file descriptors
        stdout_fd = sys.stdout.fileno()
        stderr_fd = sys.stderr.fileno()
    
        @shut_up(stderr=True)
        def test_func():
            pass
    
        test_func()
        assert not mock_stderr.called
        assert not mock_stdout.called
