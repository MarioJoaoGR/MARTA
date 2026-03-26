
# Module: pymonet.monad_try
# test_monet_try.py
from pymonet.monad_try import Try
import pytest

def test_create_successful_try():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

def test_create_failed_try():
    try_failure = Try("example", False)
    assert try_failure.value == "example"
    assert try_failure.is_success is False

def test_get_method_successful():
    try_instance = Try(42, True)
    result = try_instance.get()
    assert result == 42

def test_get_method_failed():
    try_failure = Try("example", False)
    result = try_failure.get()