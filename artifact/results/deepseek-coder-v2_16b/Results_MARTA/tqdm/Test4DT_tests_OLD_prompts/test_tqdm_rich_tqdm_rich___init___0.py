
import pytest
from unittest.mock import patch, MagicMock
from tqdm.rich import tqdm_rich  # Assuming the module is named correctly

# Test scenario 1: Basic usage of tqdm_rich with default progress configuration

# Test scenario 2: Usage of tqdm_rich with custom progress configuration

# Test scenario 3: Usage of tqdm_rich with disable=True to globally disable the progress bar
def test_tqdm_rich_disable():
    with patch('rich.progress.Progress', MagicMock()) as mock_progress:
        with tqdm_rich(total=100, disable=True) as pbar:
            assert isinstance(pbar, tqdm_rich)
            for i in range(10):
                pbar.update(1)  # This update should have no effect since disable=True
    mock_progress.assert_not_called()