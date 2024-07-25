import pytest


@pytest.fixture
def nonsense() -> list:
    return [None, 123, 1.2, "123", "bimbim", "bambam", "1234567123567123567123567123567123567123567"]
