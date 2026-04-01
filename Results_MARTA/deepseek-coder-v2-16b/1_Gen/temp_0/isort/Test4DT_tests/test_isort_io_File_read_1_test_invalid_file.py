
from pathlib import Path
from typing import Iterator, TextIO
import pytest

class File:
    stream: TextIO
    path: Path
    encoding: str
    
    def __init__(self, stream: TextIO, path: Path, encoding: str):
        self.stream = stream
        self.path = path
        self.encoding = encoding
    
    @staticmethod
    def _open(file_path: Path) -> TextIO:
        return open(file_path, 'r', encoding=file_path.name.split('.')[-1] if '.' in file_path.name else 'utf-8')
    
    @classmethod
    def read(cls, filename: str | Path) -> Iterator["File"]:
        """
        Reads a file and yields instances of the `File` class for each line in the file.
        
        This function takes a filename (either as a string or an instance of `Path`) and opens it using the `_open` method, which detects its encoding automatically. It then reads the file line by line, creating a new `File` object for each line with the detected encoding. The `File` objects are yielded one at a time during iteration.
        
        Parameters:
            filename (str | Path): The path to the file to be read. This can be either a string or an instance of the `Path` class from the standard library's `pathlib`.
            
        Yields:
            Iterator[File]: An iterator that yields instances of the `File` class, each representing a line in the file with its corresponding encoding.
            
        Raises:
            Exception: If any error occurs during the process of opening or reading the file, such as unsupported encoding or I/O errors.
            
        Example:
            >>> from pathlib import Path
            >>> try:
            ...     for file in File.read("example_file.txt"):
            ...         print(file.stream.readline())
            ... except Exception as e:
            ...     print(f"An error occurred: {e}")
        """
        file_path = Path(filename).resolve()
        stream = None
        try:
            stream = cls._open(file_path)
            for line in stream:
                yield cls(stream=stream, path=file_path, encoding=stream.encoding)
        finally:
            if stream is not None:
                stream.close()

# Test case to check the invalid file scenario
def test_invalid_file():
    with pytest.raises(Exception):
        for file in File.read("nonexistent_file.txt"):
            pass
