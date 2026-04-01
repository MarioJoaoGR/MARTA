
from typing import Optional, Union, ClassVar, Callable, overload
import time
import math
from dataclasses import field

class TimerError(Exception):
    """A custom exception used to signal timer errors."""
    pass

class Timers:
    """A class to manage multiple timers."""
    pass

class FloatArg:
    """Placeholder for a float argument."""
    pass

class Timer:
    """Time your code using a class, context manager, or decorator."""
    timers: ClassVar[Timers] = Timers()
    name: Optional[str] = None
    text: Union[str, FloatArg, Callable[[float], str]] = 'Elapsed time: {:0.4f} seconds'
    initial_text: Union[bool, str, FloatArg] = False
    logger: Optional[Callable[[str], None]] = print
    last: float = field(default=math.nan, init=False, repr=False)
    _start_time: Optional[float] = field(default=None, init=False, repr=False)
    
    def start(self) -> None:
        """Start a new timer."""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        # Log initial text when timer starts
        if self.logger and self.initial_text:
            if isinstance(self.initial_text, str):
                initial_text = self.initial_text.format(name=self.name)
            elif self.name:
                initial_text = "Timer {name} started".format(name=self.name)
            else:
                initial_text = "Timer started"
            self.logger(initial_text)

        self._start_time = time.perf_counter()

    def __enter__(self):
        """Start the timer when entering the context."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop the timer when exiting the context."""
        if hasattr(self, '_start_time'):
            elapsed_time = time.perf_counter() - self._start_time
            self.last = elapsed_time
            if self.logger:
                log_text = self.text.format(elapsed=elapsed_time) if callable(self.text) else self.text
                self.logger(log_text)
            del self._start_time

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer_start_0_test_edge_cases
codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_edge_cases.py:26:18: E3701: Invalid usage of field(), it should be used within a dataclass or the make_dataclass() function. (invalid-field-call)
codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_edge_cases.py:27:35: E3701: Invalid usage of field(), it should be used within a dataclass or the make_dataclass() function. (invalid-field-call)


"""