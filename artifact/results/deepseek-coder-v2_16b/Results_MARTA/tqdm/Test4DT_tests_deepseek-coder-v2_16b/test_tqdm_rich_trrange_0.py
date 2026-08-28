
import pytest
from tqdm import trange
from rich.progress import Progress
import time


def test_invalid_inputs():
    from tqdm import trange
    
    with pytest.raises(TypeError):
        pbar = trange(start=0, stop='a')



