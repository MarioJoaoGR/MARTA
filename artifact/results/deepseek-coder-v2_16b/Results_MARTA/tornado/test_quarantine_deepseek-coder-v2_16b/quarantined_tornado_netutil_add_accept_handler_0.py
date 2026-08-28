
import pytest
import socket
from tornado import ioloop
from typing import Callable, Any

def add_accept_handler(
    sock: socket.socket, callback: Callable[[socket.socket, Any], None]
) -> Callable[[], None]:
    """Adds an `.IOLoop` event handler to accept new connections on ``sock``.

    When a connection is accepted, the provided `callback(connection, address)` will be executed, where `connection` is a socket object and `address` is the address of the other end of the connection. This function sets up an event listener for the specified socket file descriptor to handle incoming connections. A callable is returned which removes the `.IOLoop` event handler and stops processing further incoming connections.
    """
    io_loop = ioloop.IOLoop.current()
    removed = [False]

    def accept_handler(fd: socket.socket, events: int) -> None:
        for i in range(_DEFAULT_BACKLOG):
            if removed[0]:
                return
            try:
                connection, address = sock.accept()
            except BlockingIOError:
                return
            callback(connection, address)

    def remove_handler() -> None:
        io_loop.remove_handler(sock)
        removed[0] = True

    io_loop.add_handler(sock, accept_handler, IOLoop.READ)
    return remove_handler

# Test cases for add_accept_handler function



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        import socket
        from tornado import ioloop
    
        def handle_connection(conn, addr):
            assert isinstance(conn, socket.socket), "Expected a socket object"
            assert isinstance(addr, tuple), "Expected an address tuple"
            conn.close()
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", 8888))
        sock.listen(128)
        io_loop = ioloop.IOLoop.current()
>       remove_handler = add_accept_handler(sock, handle_connection)

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py:49: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

sock = <socket.socket fd=11, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8888)>
callback = <function test_basic_usage.<locals>.handle_connection at 0x7f572ca90940>

    def add_accept_handler(
        sock: socket.socket, callback: Callable[[socket.socket, Any], None]
    ) -> Callable[[], None]:
        """Adds an `.IOLoop` event handler to accept new connections on ``sock``.
    
        When a connection is accepted, the provided `callback(connection, address)` will be executed, where `connection` is a socket object and `address` is the address of the other end of the connection. This function sets up an event listener for the specified socket file descriptor to handle incoming connections. A callable is returned which removes the `.IOLoop` event handler and stops processing further incoming connections.
        """
        io_loop = ioloop.IOLoop.current()
        removed = [False]
    
        def accept_handler(fd: socket.socket, events: int) -> None:
            for i in range(_DEFAULT_BACKLOG):
                if removed[0]:
                    return
                try:
                    connection, address = sock.accept()
                except BlockingIOError:
                    return
                callback(connection, address)
    
        def remove_handler() -> None:
            io_loop.remove_handler(sock)
            removed[0] = True
    
>       io_loop.add_handler(sock, accept_handler, IOLoop.READ)
E       NameError: name 'IOLoop' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py:31: NameError
_____________________________ test_custom_callback _____________________________

    def test_custom_callback():
        import socket
        from tornado import ioloop
    
        def handle_connection(conn, addr):
            assert isinstance(conn, socket.socket), "Expected a socket object"
            assert isinstance(addr, tuple), "Expected an address tuple"
            conn.sendall("Hello, client!\n".encode())
            conn.close()
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>       sock.bind(("localhost", 8888))
E       OSError: [Errno 98] Address already in use

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py:63: OSError
__________________________ test_additional_parameters __________________________

    def test_additional_parameters():
        import socket
        from tornado import ioloop
    
        def handle_connection(conn, addr, message):
            assert isinstance(conn, socket.socket), "Expected a socket object"
            assert isinstance(addr, tuple), "Expected an address tuple"
            conn.sendall(message.encode())
            conn.close()
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>       sock.bind(("localhost", 8888))
E       OSError: [Errno 98] Address already in use

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py:80: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py::test_basic_usage
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py::test_custom_callback
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_add_accept_handler_0.py::test_additional_parameters
============================== 3 failed in 0.11s ===============================
"""