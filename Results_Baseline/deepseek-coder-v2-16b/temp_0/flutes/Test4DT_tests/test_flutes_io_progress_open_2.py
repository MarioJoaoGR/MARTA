
import pytest
from flutes.io import progress_open
import io
from tqdm import tqdm
import functools

# Test cases for the progress_open function
def test_progress_open_with_default_parameters():
    with progress_open('example.txt', mode="r", encoding='utf-8') as f:
        assert isinstance(f, io.TextIOWrapper)