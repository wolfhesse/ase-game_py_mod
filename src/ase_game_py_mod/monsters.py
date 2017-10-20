class Monster:
    sound = 'roaring'
    color = 'blue'

    def __init__(self, hit_points=20):
        self.action_count = 0
        self.hit_points = hit_points

    def battle_cry(self):
        return self.sound.upper() + '!'

    def action(self):
        self.action_count += 1
        return f'was {self.sound}'
