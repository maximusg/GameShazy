import entity2
import explosion
import bullet
from library import *
from levelLibrary import *
import random

class BossSprite(entity2.entity2):
    def __init__(self, origin, path_to_img):
        super().__init__()
        self.image, self.rect = load_image(path_to_img)
        self.shield_gen_loc = (10,10)
        self.rect.x = origin[0]
        self.rect.y = origin[1]
        self.launchers = ((250,50),(150,75),(50,50))

        self.point_value = 50000
        self.max_health = 150
        self.health = self.max_health
        self.max_shield = 100
        self.shield = self.max_shield
        self.regen_counter = 90

        self.layer = 1
        self.dirty = 2
        self.visible = 1

    def update(self):
        self.move()
        self.regen()

        explosion_list = []
        bullet_list = []

        ##set up explosions
        if self.shield == 0:
            if random.random() < 0.05:
                explosion_list.append(explosion.ExplosionSprite(self.rect.left + self.shield_gen_loc[0]+random.randint(-2,2), self.rect.top + self.shield_gen_loc[1]+random.randint(-2,2), 'up'))
        
        if 0.25 < self.health / self.max_health <= 0.5:
            if random.random() < 0.05:
                explosion_list.append(explosion.ExplosionSprite(random.randint(self.rect.left, self.rect.right), random.randint(self.rect.top, self.rect.bottom), 'up'))
        if 0 <= self.health / self.max_health <= 0.25:
            if random.random() < 0.15:
                explosion_list.append(explosion.ExplosionSprite(random.randint(self.rect.left, self.rect.right), random.randint(self.rect.top, self.rect.bottom), 'up'))
        
        #set up bullets
        if random.random() < 0.1:
            bullet_list.append(bullet.bullet(self.rect.x+self.launchers[0][0], self.rect.y+self.launchers[0][1], 5, 'resources/weapon_images/spitfire.png', random.randint(-45,45),'vector'))

        
        return explosion_list, bullet_list
        

    def move(self):
        if self.rect.y < 300:
            self.rect = self.rect.move(0,3)
        else:
            self.rect = self.rect.move(random.randint(-2,2), random.randint(-2,2))

    def regen(self):
        if self.regen_counter == 0:
            if 0 < self.shield < self.max_shield:
                self.shield += 1
                self.regen_counter = 90
        else:
            self.regen_counter -= 1
            

    def take_damage(self, value):
        if self.shield > 0:
            self.shield -= value
        else:
            self.health -= value
        if self.health <= 0:
            self.visible = 0
        

        