import pytest

from ase_game_py_mod import monsters


@pytest.fixture()
def monster():
    return monsters.Monster()
