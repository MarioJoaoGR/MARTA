
# Module: flutes.multiproc
# test_flutes_multiproc.py
import pytest
from flutes.multiproc import ProgressBarManager

def test_ProgressBarManager_enter():
    manager = ProgressBarManager(verbose=True)
    assert isinstance(manager.__enter__(), ProgressBarManager)
