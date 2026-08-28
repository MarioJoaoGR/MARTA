
import pytest
from pysnooper.tracer import Tracer, CommonVariable, BaseVariable, Exploding
import threading
import os

def test_tracer_initialization_default():
    tracer = Tracer()
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info is False
    assert tracer.max_variable_length == 100
    assert tracer.relative_time is False

def test_tracer_initialization_with_output_file():
    output_path = 'test_trace.log'
    tracer = Tracer(output=output_path)
    assert callable(tracer._write)  # _write should be a callable function