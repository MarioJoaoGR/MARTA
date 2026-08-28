
import pytest
from tqdm import tqdm

# Test _repr_pretty_ with default settings
def test_progressbar__repr_pretty_default():
    progress_bar = tqdm(total=100)
    assert "tqdm" in repr(progress_bar), "The repr should include 'tqdm' for default representation."
    progress_bar.close()

# Test _repr_pretty_ with detailed setting
def test_progressbar__repr_pretty_detailed():
    progress_bar = tqdm(total=100)
    assert "tqdm" in repr(progress_bar), "The repr should include 'tqdm' when detailed is set to True."
    progress_bar.close()
