
import pytest
from flutes.io import progress_open
import io
from typing import Optional, Callable
from tqdm import tqdm

def test_valid_case():
    path = "testfile.txt"
    mode = "r"
    encoding = 'utf-8'
    verbose = True
    buffer_size = io.DEFAULT_BUFFER_SIZE
    bar_fn: Optional[Callable] = None
    
    with progress_open(path, mode=mode, encoding=encoding, verbose=verbose, buffer_size=buffer_size, bar_fn=bar_fn) as f:
        assert isinstance(f, io.TextIOWrapper)
        assert hasattr(f, 'progress_bar')
        assert isinstance(f.progress_bar, tqdm)
