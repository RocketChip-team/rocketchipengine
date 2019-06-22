from Scripts.Tile import *


class GameObject:
    def __init__(self, x, y, sheet, palette, gravity, size, animated, tag, behaviours, latency=5):
        self.x = x
        self.y = y
        self.gravity = gravity
        self.vx = 0
        self.vy = 0
        self.animated = animated
        if animated == True:
            self.sprite = AnimatedMetaTile(0, 0, sheet, palette, size, tag, latency, flipx=0, flipy=0, swap=0)
        else:
            indexes = []
            flips = []
            for y in range(size[1]):
                for x in range(size[0]):
                    indexes.append(0)
                    flips.append(0)
            self.sprite = MetaTile(0, 0, sheet, palette, indexes, flips, size, tag)
        self.colliders = []
        self.controller = None
        self.behaviours = behaviours
        self.behnames = self.behaviours.keys()
        self.surface = pygame.Surface((size[0]*8, size[1]*8))

    def add_behaviour(self, name, behaviour):
        self.behaviours[name] = behaviour
        self.behnames.append(name)

    def update(self, game):
        if self.controller:
            self.controller.update(game.levents)
        if self.colliders:
            self.colliders.update(game)
        for i in self.behnames:
            exec(self.behaviours[i])

    def draw(self, surface):
        self.sprite.draw(self.surface)
        surface.blit(self.surface, (self.x, self.y))