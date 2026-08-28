
import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado.gen import multi, sleep

def test_event_wait():
    event = Event()
    
    async def waiter():
        print("Waiting for event")
        await event.wait()
        print("Event has been set, continuing execution")
    
    async def setter():
        print("About to set the event")
        event.set()
    
    async def runner():
        await multi([waiter(), setter()])
    
    IOLoop.current().run_sync(runner)


def test_event_multiple_coroutines():
    event = Event()
    
    async def waiter1():
        print("Waiter 1 waiting for the event")
        await event.wait()
        print("Waiter 1: Event has been set, continuing execution")
    
    async def waiter2():
        print("Waiter 2 waiting for the event")
        await event.wait()
        print("Waiter 2: Event has been set, continuing execution")
    
    async def setter():
        print("About to set the event")
        event.set()
    
    async def runner():
        await multi([waiter1(), waiter2(), setter()])
    
    IOLoop.current().run_sync(runner)