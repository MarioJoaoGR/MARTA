
import pytest

class WritableStream:
    def write(self, s):
        """
        Writes a string to the output stream. This method is intended to be overridden in subclasses.
        """
        pass

class ConsoleWriter(WritableStream):
    def __init__(self):
        self.output = []

    def write(self, s):
        self.output.append(s)

def test_console_writer_write():
    console_writer = ConsoleWriter()
    console_writer.write("Hello, world!")
    assert console_writer.output == ["Hello, world!"]

def test_console_writer_multiple_writes():
    console_writer = ConsoleWriter()
    console_writer.write("First line.")
    console_writer.write("Second line.")
    assert console_writer.output == ["First line.", "Second line."]
