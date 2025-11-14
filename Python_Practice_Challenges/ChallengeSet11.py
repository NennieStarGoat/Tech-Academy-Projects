class Bun:
    def __init__(self, name, fluff_levels, position, ear_type):
        self.name = name
        self.fluff_levels = fluff_levels
        self.position = position
        self.ear_type = ear_type


class Royalty(Bun):
    carrot_coins = 1000
    status = ''


class Commoner(Bun):
    defenestration_count = 0


Bun_King = Royalty('Bun Bun', 'soft and tufty', 'King', 'flopsy')
Bun_King.carrot_coins = 10000005
Bun_King.status = 'Tyrant'

Ruffletum = Royalty('Ruffletum Tumblesnoot', 'extremely ruffled and good', 'Queen', 'big like a hare\'s')
Ruffletum.carrot_coins = 10000005
Ruffletum.status = 'Defender of Bundom'

Mopsy = Commoner('Mopsy', 'long and floofy', 'Peasant', 'alert')
Mopsy.defenestration_count = 41

print(Bun_King.__dict__)
print(Ruffletum.__dict__)
print(Mopsy.__dict__)
