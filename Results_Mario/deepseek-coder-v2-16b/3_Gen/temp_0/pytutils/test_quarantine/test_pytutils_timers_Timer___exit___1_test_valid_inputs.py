
import time
from pytutils.timers import Timer  # Assuming this module contains the Timer class definition

class Timer:
    """
    Context manager that times its execution.
    
    This class provides a simple way to measure the duration of code execution within a with statement. It can be used to time any block of code or function, and optionally log the elapsed time if verbose mode is enabled.
    
    Parameters:
        name (str): An optional string that represents the name associated with the timer for logging purposes. Default is an empty string.
        verbose (bool): A boolean flag indicating whether to print the elapsed time in milliseconds after the execution of the timed block. Default is False.
        
    Example usage:
    
    ```python
    from some_module import Timer
    
    with Timer(name='Operation', verbose=True) as t:
        # Your code to be timed goes here
        time.sleep(1)  # Example operation that takes 1 second
        
    # Output will be something like: Operation: Elapsed time: 1000.000000 ms
    ```
    
    In this example, the Timer context manager is used to time a block of code where `time.sleep(1)` is executed. The elapsed time in milliseconds is printed if verbose mode is enabled.
    
    __exit__ method:
    -----------
    This method is called when exiting the managed context and records the elapsed time in milliseconds if verbose mode is enabled.
    
    Parameters:
        *args (tuple): Variable length argument list, typically used to capture exception information.
        
    Returns:
        None
    """
    def __init__(self, name='', verbose=False):
        self.name = name
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs

        if self.verbose:
            print(f'{self.name}: Elapsed time: {self.msecs} ms')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_timers_Timer___exit___1_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___1_test_valid_inputs.py:5:0: E0102: class already defined line 3 (function-redefined)


"""