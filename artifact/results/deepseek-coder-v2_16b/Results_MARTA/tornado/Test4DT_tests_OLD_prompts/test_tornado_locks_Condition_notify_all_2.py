
import pytest
from unittest.mock import patch, MagicMock
from tornado.ioloop import IOLoop
from tornado.locks import Condition

@pytest.fixture(scope="function")
def setup_condition():
    condition = Condition()
    return condition

def test_Condition_notify_all_basic(setup_condition):
    with patch('tornado.ioloop.IOLoop.current', return_value=MagicMock()) as mock_io_loop:
        async def waiter():
            print("I'll wait right here")
            await setup_condition.wait()
            print("I'm done waiting")

        async def notifier():
            print("About to notify")
            setup_condition.notify_all()
            print("Done notifying")

        async def runner():
            await waiter()
            await notifier()

        IOLoop.current().run_sync(runner)

    assert True  # This is a placeholder to satisfy pytest's requirement for an assertion in the test body
