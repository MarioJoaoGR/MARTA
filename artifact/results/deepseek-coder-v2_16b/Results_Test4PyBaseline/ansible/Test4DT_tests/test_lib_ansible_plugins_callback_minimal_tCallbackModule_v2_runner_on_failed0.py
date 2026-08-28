# Module: ansible.plugins.callback.minimal
import pytest
from ansible.plugins.callback import minimal

# Assuming the module is imported correctly and available as `minimal`
CallbackModule = minimal.CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.mark.parametrize("result, ignore_errors, expected", [
    (
        {
            '_host': {'get_name': lambda: 'localhost'},
            '_task': {'action': 'some_action'},
            '_result': {'stdout': 'Output', 'stderr': 'Error', 'rc': 1}
        },
        False,
        "localhost | FAILED! => Output\n"
    ),
    (
        {
            '_host': {'get_name': lambda: 'localhost'},
            '_task': {'action': 'some_action'},
            '_result': {'stdout': '', 'stderr': 'Error', 'rc': 1}
        },
        False,
        "localhost | FAILED! => Error\n"
    ),
    (
        {
            '_host': {'get_name': lambda: 'localhost'},
            '_task': {'action': 'some_action'},
            '_result': {'stdout': '', 'stderr': 'Error', 'rc': 1}
        },
        True,
        None
    )
])
def test_v2_runner_on_failed(callback_module, result, ignore_errors, expected):
    if expected is not None:
        from io import StringIO
        captured_output = StringIO()
        callback_module._display.display = lambda x, color=None: print(x, file=captured_output)
        
        callback_module.v2_runner_on_failed(result, ignore_errors)
        assert captured_output.getvalue().strip() == expected.strip()
    else:
        # When ignore_errors is True, no output should be produced
        with pytest.raises(AssertionError):  # Assuming the method raises an error when it shouldn't
            callback_module.v2_runner_on_failed(result, ignore_errors)
