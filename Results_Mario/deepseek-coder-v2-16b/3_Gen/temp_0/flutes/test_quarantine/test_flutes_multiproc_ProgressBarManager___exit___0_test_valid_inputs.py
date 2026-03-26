
import pytest
from flutes.multiproc import ProgressBarManager
import time
import random
import functools
import flutes

# Assuming data is defined somewhere in the test module or imported from a fixture
data = [list(range(100)) for _ in range(4)]  # Example data for testing

def run(xs: list, *, bar):
    result = 0
    for idx, x in enumerate(xs):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1, postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    return result

def run2(xs: list, *, bar):
    result = 0
    for idx, x in enumerate(bar.iter(xs)):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    return result

@pytest.fixture
def manager():
    return ProgressBarManager()

def test_valid_inputs(manager):
    run_fn = functools.partial(run, bar=manager.proxy)
    with flutes.safe_pool(4) as pool:
        for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
            flutes.log(f"Processed {idx + 1} arrays")
