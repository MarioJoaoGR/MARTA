
import os
import pickle
from pathlib import Path
from typing import Optional, Callable
import pytest
from flutes.fs import cache

@cache(path=None, verbose=False)
def cached_function():
    return 'This will be executed every time.'

def test_edge_case():
    result = cached_function()
    assert result == 'This will be executed every time.', "The function should execute and return the expected string."
