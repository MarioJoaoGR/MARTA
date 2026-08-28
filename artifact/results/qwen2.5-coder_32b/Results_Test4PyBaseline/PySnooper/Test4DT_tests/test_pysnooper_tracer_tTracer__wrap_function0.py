
# Test case  

# Module: pysnooper.tracer
import pytest
from pysnooper.tracer import Tracer, CommonVariable, Exploding

def test_tracer_initialization_default():
    tracer = Tracer()
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info is False
    assert tracer.max_variable_length == 100
    assert tracer.normalize is False
    assert tracer.relative_time is False

def test_tracer_initialization_with_output_file():
    tracer = Tracer(output='test.log')
    assert tracer._write.__name__ == 'write'

def test_tracer_initialization_with_watch_variables():
    tracer = Tracer(watch=('x', 'y'))
    assert len(tracer.watch) == 2
    assert all(isinstance(v, (CommonVariable, Exploding)) for v in tracer.watch)

def test_tracer_initialization_with_watch_explode():
    tracer = Tracer(watch_explode=('data',))
    assert len(tracer.watch) == 1
    assert isinstance(tracer.watch[0], Exploding)

def test_tracer_initialization_with_depth():
    tracer = Tracer(depth=3)
    assert tracer.depth == 3

def test_tracer_initialization_with_prefix():
    tracer = Tracer(prefix='DEBUG ')
    assert tracer.prefix == 'DEBUG '

def test_tracer_initialization_with_overwrite():
    tracer = Tracer(output='test.log', overwrite=True)
    assert tracer._write.__name__ == 'write'

def test_tracer_initialization_with_thread_info():
    tracer = Tracer(thread_info=True)
    assert tracer.thread_info is True

def test_tracer_initialization_with_custom_repr():
    def custom_repr_func(value):
        return f"Custom: {value}"
    
    tracer = Tracer(custom_repr=((int, custom_repr_func),))
    assert len(tracer.custom_repr) == 1
    assert tracer.custom_repr[0][0] is int

def test_tracer_initialization_with_max_variable_length():
    tracer = Tracer(max_variable_length=200)
    assert tracer.max_variable_length == 200

def test_tracer_initialization_with_normalize():
    tracer = Tracer(normalize=True)
    assert tracer.normalize is True

def test_tracer_initialization_with_relative_time():
    tracer = Tracer(relative_time=True)
    assert tracer.relative_time is True
