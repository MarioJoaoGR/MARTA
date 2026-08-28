
import pytest
from ansible.module_utils.connection import send_data
import socket
import struct

@pytest.fixture(scope="function")
def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    yield sock
    sock.close()



def test_valid_list_input(create_socket):
    sock = create_socket
    data = [1, 2, 3]
    with pytest.raises(TypeError):
        send_data(sock, data)