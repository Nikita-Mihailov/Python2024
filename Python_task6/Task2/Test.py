import pytest


@pytest.fixture(autouse=True)
def my_fixture():
    with open("file_test1.txt", "r") as f:
        pass

    with open("file_test2.txt", "r") as f:
        pass

    with open("output_file.txt", "w") as f:
        pass
