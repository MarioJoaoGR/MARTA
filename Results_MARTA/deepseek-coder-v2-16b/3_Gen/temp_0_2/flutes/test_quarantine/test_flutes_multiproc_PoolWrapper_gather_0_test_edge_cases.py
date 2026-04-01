
import pytest
from flutes.multiproc import PoolWrapper

def mock_fn(x):
    yield x * 2

@pytest.fixture
def pool():
    return PoolWrapper()

def test_gather(pool):
    results = pool.gather(mock_fn, [1, 2, 3], chunksize=1)
    assert list(results) == [2, 4, 6]

def test_gather_with_args(pool):
    def mock_fn_with_args(x, multiplier):
        yield x * multiplier
    
    results = pool.gather(mock_fn_with_args, [1, 2, 3], chunksize=1, args=(2,))
    assert list(results) == [2, 4, 6]

def test_gather_with_kwds(pool):
    def mock_fn_with_kwds(x, multiplier=1):
        yield x * multiplier
    
    results = pool.gather(mock_fn_with_kwds, [1, 2, 3], chunksize=1, kwds={'multiplier': 2})
    assert list(results) == [2, 4, 6]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_gather_with_args _____________________________

self = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>
fn = <function test_gather_with_args.<locals>.mock_fn_with_args at 0x7f6a2a604f40>
iterable = [1, 2, 3], chunksize = 1, args = (2,), kwds = {}

    def gather(self, fn: Callable[[T], Iterator[R]], iterable: Iterable[T], chunksize: int = 1,
               args: Iterable[Any] = (), kwds: Dict[str, Any] = {}) -> Iterator[R]:
        # Refer to documentation at `PoolType.gather`.
        ctx = mp.get_context()
        ctx.reducer = CustomMPReducer  # type: ignore[assignment]
        with ctx.Manager() as manager:
            queue = manager.Queue()
            gather_fn = functools.partial(_gather_fn, queue, fn)
            if not isinstance(iterable, list):
                iterable = list(iterable)
            length = len(iterable)
            end_count = 0
            ret = self.map_async(  # type: ignore[call-arg]
                gather_fn, iterable, chunksize=chunksize, args=args, kwds=kwds)
            while True:
                try:
>                   x = queue.get_nowait()

flutes/flutes/multiproc.py:284: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <AutoProxy[Queue] object, typeid 'Queue' at 0x7f6a2a6b7450>
methodname = 'get_nowait', args = (), kwds = {}

    def _callmethod(self, methodname, args=(), kwds={}):
        '''
        Try to call a method of the referent and return a copy of the result
        '''
        try:
            conn = self._tls.connection
        except AttributeError:
            util.debug('thread %r does not own a connection',
                       threading.current_thread().name)
            self._connect()
            conn = self._tls.connection
    
        conn.send((self._id, methodname, args, kwds))
        kind, result = conn.recv()
    
        if kind == '#RETURN':
            return result
        elif kind == '#PROXY':
            exposed, token = result
            proxytype = self._manager._registry[token.typeid][-1]
            token.address = self._token.address
            proxy = proxytype(
                token, self._serializer, manager=self._manager,
                authkey=self._authkey, exposed=exposed
                )
            conn = self._Client(token.address, authkey=self._authkey)
            dispatch(conn, None, 'decref', (token.id,))
            return proxy
>       raise convert_to_error(kind, result)
E       _queue.Empty

/usr/local/lib/python3.11/multiprocessing/managers.py:837: Empty

During handling of the above exception, another exception occurred:

pool = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_gather_with_args(pool):
        def mock_fn_with_args(x, multiplier):
            yield x * multiplier
    
        results = pool.gather(mock_fn_with_args, [1, 2, 3], chunksize=1, args=(2,))
>       assert list(results) == [2, 4, 6]

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:288: in gather
    new_length = sum(map(bool, ret.get()))
/usr/local/lib/python3.11/multiprocessing/pool.py:774: in get
    raise self._value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (1, 0, <function mapstar at 0x7f6a2a364720>, ((<flutes.multiproc.FuncWrapper object at 0x7f6a2a6b7750>, (1,)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_gather_with_args.<locals>.mock_fn_with_args'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
____________________________ test_gather_with_kwds _____________________________

self = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>
fn = <function test_gather_with_kwds.<locals>.mock_fn_with_kwds at 0x7f6a2a6613a0>
iterable = [1, 2, 3], chunksize = 1, args = (), kwds = {'multiplier': 2}

    def gather(self, fn: Callable[[T], Iterator[R]], iterable: Iterable[T], chunksize: int = 1,
               args: Iterable[Any] = (), kwds: Dict[str, Any] = {}) -> Iterator[R]:
        # Refer to documentation at `PoolType.gather`.
        ctx = mp.get_context()
        ctx.reducer = CustomMPReducer  # type: ignore[assignment]
        with ctx.Manager() as manager:
            queue = manager.Queue()
            gather_fn = functools.partial(_gather_fn, queue, fn)
            if not isinstance(iterable, list):
                iterable = list(iterable)
            length = len(iterable)
            end_count = 0
            ret = self.map_async(  # type: ignore[call-arg]
                gather_fn, iterable, chunksize=chunksize, args=args, kwds=kwds)
            while True:
                try:
>                   x = queue.get_nowait()

flutes/flutes/multiproc.py:284: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <AutoProxy[Queue] object, typeid 'Queue' at 0x7f6a2a4cd7d0>
methodname = 'get_nowait', args = (), kwds = {}

    def _callmethod(self, methodname, args=(), kwds={}):
        '''
        Try to call a method of the referent and return a copy of the result
        '''
        try:
            conn = self._tls.connection
        except AttributeError:
            util.debug('thread %r does not own a connection',
                       threading.current_thread().name)
            self._connect()
            conn = self._tls.connection
    
        conn.send((self._id, methodname, args, kwds))
        kind, result = conn.recv()
    
        if kind == '#RETURN':
            return result
        elif kind == '#PROXY':
            exposed, token = result
            proxytype = self._manager._registry[token.typeid][-1]
            token.address = self._token.address
            proxy = proxytype(
                token, self._serializer, manager=self._manager,
                authkey=self._authkey, exposed=exposed
                )
            conn = self._Client(token.address, authkey=self._authkey)
            dispatch(conn, None, 'decref', (token.id,))
            return proxy
>       raise convert_to_error(kind, result)
E       _queue.Empty

/usr/local/lib/python3.11/multiprocessing/managers.py:837: Empty

During handling of the above exception, another exception occurred:

pool = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_gather_with_kwds(pool):
        def mock_fn_with_kwds(x, multiplier=1):
            yield x * multiplier
    
        results = pool.gather(mock_fn_with_kwds, [1, 2, 3], chunksize=1, kwds={'multiplier': 2})
>       assert list(results) == [2, 4, 6]

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:288: in gather
    new_length = sum(map(bool, ret.get()))
/usr/local/lib/python3.11/multiprocessing/pool.py:774: in get
    raise self._value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (2, 0, <function mapstar at 0x7f6a2a364720>, ((<flutes.multiproc.FuncWrapper object at 0x7f6a2a4ce510>, (1,)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_gather_with_kwds.<locals>.mock_fn_with_kwds'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py::test_gather_with_args
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py::test_gather_with_kwds
========================= 2 failed, 1 passed in 0.89s ==========================

Exception ignored in: <function Pool.__del__ at 0x7f6a2a3679c0>
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 271, in __del__
    self._change_notifier.put(None)
  File "/usr/local/lib/python3.11/multiprocessing/queues.py", line 377, in put
    self._writer.send_bytes(obj)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 200, in send_bytes
    self._send_bytes(m[offset:offset + size])
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 427, in _send_bytes
    self._send(header + buf)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 384, in _send
    n = write(self._handle, buf)
        ^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 9] Bad file descriptor
"""