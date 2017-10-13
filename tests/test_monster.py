import unittest

from game import monsters


def test_default(monster):
    assert monster.sound == 'roaring'
    assert monster.hit_points == 20


def test_color(monster):
    assert monster.color == 'blue'


def test_hitpoints(monster):
    assert monster.hit_points == 20


def test_battle_cry(monster):
    assert monster.battle_cry() == 'ROARING'


class TestMonsterUnittest(unittest.TestCase):
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
