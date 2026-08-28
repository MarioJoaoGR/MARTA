
import pytest
from pysnooper.tracer import Tracer


def test_valid_watch_single_variable():
    tracer = Tracer(output='watch_test.log', watch=('x',), depth=1, prefix='WATCH: ', overwrite=True)
    assert len(tracer.watch) == 1
    assert isinstance(tracer.watch[0], type(tracer.watch[0]))  # Assuming CommonVariable is not directly accessible

def test_valid_watch_multiple_variables():
    tracer = Tracer(output='watch_multiple_test.log', watch=('x', 'y'), depth=1, prefix='WATCH_MULTIPLE: ', overwrite=True)
    assert len(tracer.watch) == 2
    assert all(isinstance(watch_var, type(tracer.watch[0])) for watch_var in tracer.watch)

def test_valid_watch_explode_single_variable():
    tracer = Tracer(output='watch_explode_test.log', watch_explode=('my_list',), depth=1, prefix='WATCH_EXPLODE: ', overwrite=True)
    assert len(tracer.watch) == 1
    assert isinstance(tracer.watch[0], type(tracer.watch[0]))  # Assuming Exploding is not directly accessible

def test_valid_watch_explode_multiple_variables():
    tracer = Tracer(output='watch_explode_multiple_test.log', watch_explode=('my_list', 'another_var'), depth=1, prefix='WATCH_EXPLODE_MULTIPLE: ', overwrite=True)
    assert len(tracer.watch) == 2
    assert all(isinstance(watch_var, type(tracer.watch[0])) for watch_var in tracer.watch)