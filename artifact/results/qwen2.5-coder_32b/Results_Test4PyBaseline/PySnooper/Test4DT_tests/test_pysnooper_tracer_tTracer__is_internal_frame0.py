
import pytest
from pysnooper.tracer import Tracer, CommonVariable, Exploding

def test_tracer_initialization_with_watch_and_watch_explode():
    tracer = Tracer(watch=('x',), watch_explode=('y',))
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], CommonVariable)
    assert isinstance(tracer.watch[1], Exploding)

def test_tracer_initialization_with_empty_watch_and_explode():
    tracer = Tracer(watch=(), watch_explode=())
    assert len(tracer.watch) == 0

def test_tracer_initialization_with_mixed_types_in_watch():
    tracer = Tracer(watch=('x', CommonVariable('y')))
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], CommonVariable)
    assert isinstance(tracer.watch[1], CommonVariable)

def test_tracer_initialization_with_mixed_types_in_watch_explode():
    tracer = Tracer(watch_explode=('my_dict', Exploding('my_list')))
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], Exploding)
    assert isinstance(tracer.watch[1], Exploding)

def test_tracer_initialization_with_predefined_basevariable():
    tracer = Tracer(watch=(CommonVariable('x'),), watch_explode=(Exploding('y'),))
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], CommonVariable)
    assert isinstance(tracer.watch[1], Exploding)

def test_tracer_initialization_with_invalid_watch_elements():
    with pytest.raises(TypeError):
        tracer = Tracer(watch=(123,))  # Invalid type

def test_tracer_initialization_with_invalid_watch_explode_elements():
    with pytest.raises(TypeError):
        tracer = Tracer(watch_explode=(456,))  # Invalid type
