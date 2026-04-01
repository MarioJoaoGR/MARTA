
import pytest
from flutes.multiproc import PoolWrapper
import multiprocessing as mp
import functools
from typing import Callable, Iterator, Iterable, Any, Dict

def test_valid_inputs():
    pool = PoolWrapper()
    
    # Define a simple function to use with the gather method
    def square(x):
        return x * x
    
    # Test with an iterable of numbers and the square function
    results = list(pool.gather(square, range(10), chunksize=2))
    
    # Expected results from squaring each number in the range
    expected_results = [x ** 2 for x in range(10)]
    
    assert results == expected_results

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

self = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>
fn = <function test_valid_inputs.<locals>.square at 0x7f9406da9300>
iterable = [0, 1, 2, 3, 4, 5, ...], chunksize = 2, args = (), kwds = {}

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

self = <AutoProxy[Queue] object, typeid 'Queue' at 0x7f9406e51990>
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

    def test_valid_inputs():
        pool = PoolWrapper()
    
        # Define a simple function to use with the gather method
        def square(x):
            return x * x
    
        # Test with an iterable of numbers and the square function
>       results = list(pool.gather(square, range(10), chunksize=2))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_valid_inputs.py:16: 
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
obj = (0, 0, <function mapstar at 0x7f9406ba4220>, ((functools.partial(<function _gather_fn at 0x7f9406bda5c0>, <AutoProxy[Q...ect, typeid 'Queue' at 0x7f9406e51990>, <function test_valid_inputs.<locals>.square at 0x7f9406da9300>), (0, 1)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_valid_inputs.<locals>.square'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.36s ===============================
"""