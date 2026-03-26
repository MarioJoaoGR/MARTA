
import pytest
from codetiming import Timer

def test_edge_cases():
    # Test None and empty values for optional parameters
    
    # Test with all optional parameters set to their default or None values
    timer = Timer()
    assert timer.name is None
    assert timer.text == 'Elapsed time: {:0.4f} seconds'
    assert not timer.initial_text  # This should be False, not a string comparison
    assert timer.logger == print
    
    # Test with name set to None
    timer_none_name = Timer(name=None)
    assert timer_none_name.name is None
    
    # Test with text set to a callable function
    def custom_text_function(elapsed):
        return f'Custom time: {elapsed:.4f} seconds'
    timer_custom_text = Timer(text=custom_text_function)
    assert callable(timer_custom_text.text)
    
    # Test with initial_text set to True
    timer_true_initial_text = Timer(initial_text=True)
    assert timer_true_initial_text.initial_text is True  # Correct assertion for boolean value
