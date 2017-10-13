import pytest

from game import monsters


@pytest.fixture()
def monster():
    return monsters.Monster()
