
import sys
from IPython.core import ultratb
from flutes.exception import BdbQuit

def register_ipython_excepthook(capture_keyboard_interrupt: bool = False) -> None:
    r"""Register an exception hook that launches an interactive IPython session upon uncaught exceptions.

    :param capture_keyboard_interrupt: If ``False``, an uncaught :py:exc:`KeyboardInterrupt` exception will not trigger
        the IPython debugger. Defaults to ``False``.
    """
    skip_exceptions = [BdbQuit]
    if not capture_keyboard_interrupt:
        skip_exceptions.append(KeyboardInterrupt)

    def excepthook(type, value, traceback):
        if any(type is exc_type for exc_type in skip_exceptions):
            # Don't capture keyboard interrupts (Ctrl+C) or Python debugger exit events.
            sys.__excepthook__(type, value, traceback)
        else:
            ipython_hook = ultratb.FormattedTB(mode='Context', color_scheme='Linux', call_pdb=1)
            ipython_hook(type, value, traceback)

    # Enter IPython debugger on exception.
    sys.excepthook = excepthook

# Test case for register_ipython_excepthook function
def test_register_ipython_excepthook():
    from flutes.exception import BdbQuit
    import pytest

    # Mock the IPython ultratb module
    class FakeIPythonHook:
        def __call__(self, *args):
            pass

    sys.modules['IPython.core.ultratb'] = FakeIPythonHook()

    # Test with capture_keyboard_interrupt=True
    register_ipython_excepthook(capture_keyboard_interrupt=True)
    assert hasattr(sys, 'excepthook')

    # Test with capture_keyboard_interrupt=False
    register_ipython_excepthook(capture_keyboard_interrupt=False)
    assert hasattr(sys, 'excepthook')

    # Test handling of KeyboardInterrupt when capture_keyboard_interrupt is False
    def raise_keyboard_interrupt():
        raise KeyboardInterrupt()

    with pytest.raises(KeyboardInterrupt):
        register_ipython_excepthook(capture_keyboard_interrupt=False)
        raise_keyboard_interrupt()
