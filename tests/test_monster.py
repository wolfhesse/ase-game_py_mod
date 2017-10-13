import unittest

import pytest as pytest

from ase_game import monsters


@pytest.mark.parametrize('monster, expected', [
    (monsters.Monster(), 20),
    (monsters.Monster(hit_points=22), 22),
])
def test_default(monster, expected):  # pragma for coverage?
    # inputs, why?, expected results
    """
    Default Monster class should hva a 'roar' sound
    and 20 hit points
    :param monster:
    :return:
    """
    assert monster.sound == 'roaring'
    assert monster.hit_points == expected


def test_color(monster):
    assert monster.color == 'blue'


def test_hitpoints(monster):
    assert monster.hit_points == 20


def test_battle_cry(monster):
    assert monster.battle_cry() == 'ROARING!'


def test_battle_cry_alt(monster):
    assert monster.battle_cry() == monster.sound.upper()
    assert monster.battle_cry() + "a" == monster.sound.upper() + "a"


class TestMonsterUnit(unittest.TestCase):
    def test_default(self):
        monster = monsters.Monster()
        self.assertEqual(20, monster.hit_points)
        self.assertEqual('roaring', monster.sound)

    def test_custom_hit_points(self):
        monster = monsters.Monster(hit_points=200)
        self.assertEqual(200, monster.hit_points)

    def test_monster_action(self):
        monster = monsters.Monster()
        action_result = monster.action()
        self.assertEqual('was roaring', action_result)
        self.assertEqual(1, monster.action_count)
