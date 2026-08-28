
import pytest
from pymonet.monad_try import Try


def test_failed_init():
    try_failure = Try("error", False)
    assert try_failure.is_success is False