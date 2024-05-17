import pytest
from Task2 import merge_and_write


def test_merge_and_write():
    assert merge_and_write("file_test1.txt", "file_test2.txt", "output_file.txt") == "Hello World"
    assert merge_and_write("file_test12.txt", "file_test2.txt", "output_file.txt") == "Один из файлов не найден"


test_merge_and_write()
