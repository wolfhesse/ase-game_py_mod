import pytest

from ase_game import monsters


@pytest.fixture()
def monster():
    return monsters.Monster()
