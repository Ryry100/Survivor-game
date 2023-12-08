from pgzrun import go

from random import randint
from pgzhelper import *
WIDTH = 1792
HEIGHT = 896
TITLE = "Tiny Survivor"

enemies= [Actor('evil_wizard')]
timer = 10


#actors
player = Actor("wizard", (WIDTH / 2, HEIGHT / 2))
player.speed = 3
player.transparency = 255


green_guy = Actor("green_guy", (randint(1000, 2000), randint(1, 1000)))
green_guy.speed = 2
green_guy.is_visible= False

wizard_speed = 2
axe_timer = 100 
weapons = []

def axe_attack():
    weapons[0].angle = 90
    weapons.pop(0)




def add_enemy():
    wizard = Actor("evil_wizard", (randint(1000, 2000), randint(1, 1000)))
    wizard.speed = 2
    enemies.append(wizard)

def get_closest_enemy():
    closest = enemies[0]
    if len(enemies) > 0:    
        for enemy in enemies:
            if player.distance_to(enemy) < player.distance_to(closest):
                closest = enemy
                print(player.distance_to(closest))
        return closest


def add_weapon():
    global axe_timer
    axe_timer -= 1
    if axe_timer <= 0 and len(enemies):
        axe_timer = 300
        axe = Actor("axe", get_closest_enemy().pos)
        
        if len(weapons) >= 1:
            weapons.pop(0)
        weapons.append(axe)

def move():
    if keyboard.a:
        #move left
        player.x -= player.speed
    if keyboard.w:
        player.y -= player.speed
    if keyboard.d:
        player.x += player.speed
    if keyboard.s:
        player.y += player.speed
def bound_player():
    if player.left <= 128:
        player.left = 128
    if player.right >= WIDTH - 128:
        player.right = WIDTH-128
    if player.top <= 115:
        player.top = 115
    if player.bottom >= HEIGHT - 128:
        player.bottom = HEIGHT - 128

def draw():
    screen.blit("dungeon1", (0,0))
    for enemy in enemies:
        enemy.draw()
    player.draw()
    if green_guy.is_visible:

        green_guy.draw()
    for weapon in weapons:
        weapon.draw()
    



def update():
    move()
    global timer
    global wizard_speed
    player.transparency -= 1
    if player.transparency <= 0:
         player.transparency =255
    timer -= 1
    add_weapon()
    for enemy in enemies:
        if enemy.collidelist(weapons)!= -1:
            
            enemy.transparency -= 5
            if enemy.transparency <= 0:
                enemies.remove(enemy)
                wizard_speed + 1
            clock.schedule_unique(axe_attack, 0.599999999999999999999999999999999)
        enemy.move_towards(player, wizard_speed)
    if timer <= 0:
        timer = 60
        add_enemy()

    green_guy.move_towards(player, green_guy.speed)
    if keyboard.space:
        green_guy.is_visible= True
    bound_player()
    
    


#last line
go()
