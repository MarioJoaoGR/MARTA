
# Test case  

import pytest
from pysnooper.tracer import Tracer, CommonVariable  # Importing CommonVariable along with Tracer
import inspect  # Importing inspect module for frame inspection
import sys      # Importing sys module to access trace functions

def test_tracer_initialization_default():
    tracer = Tracer()
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info is False
    assert tracer.max_variable_length == 100
    assert tracer.normalize is False
    assert tracer.relative_time is False

def test_tracer_initialization_with_output_file():
    tracer = Tracer(output='trace.log')
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info is False
    assert tracer.max_variable_length == 100
    assert tracer.normalize is False
    assert tracer.relative_time is False

def test_tracer_initialization_with_watch():
    tracer = Tracer(watch=('x', 'y'))
    assert len(tracer.watch) == 2