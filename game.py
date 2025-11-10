import pygame
import random

pygame.init()
try:
    pygame.mixer.init()
except:
    pass

#display
W, H = 720, 480
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Iron Man Shooter")
clock = pygame.time.Clock()

#image
player_img = pygame.image.load(r"D:\Studies\Projects\Python\College_files\Images\player.png")
enemy_img = pygame.image.load(r"D:\Studies\Projects\Python\College_files\Images\eneemy.png")
bullet_img = pygame.image.load(r"D:\Studies\Projects\Python\College_files\Images\bullet.png")
bg_img = pygame.image.load(r"D:\Studies\Projects\Python\College_files\Images\Bg.jpg")
bg_img = pygame.transform.scale(bg_img, (W, H))

#image scale
player_img = pygame.transform.scale(player_img, (60, 60))
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (30, 30))

#set player position
player = player_img.get_rect(center=(60, H//2))

#mp3
shoot_sound = pygame.mixer.Sound(r"D:\Studies\Projects\Python\College_files\Images\Shhot.mp3")
explosion_sound = pygame.mixer.Sound(r"D:\Studies\Projects\Python\College_files\Images\Explosion.mp3")

#variables
bullets = []
enemies = []
explosions = []
score = 0
spawn_time = 0
game_over = False
player_health = 100

font = pygame.font.SysFont(None, 40)

#explosion function
def create_explosion(x, y):
    explosions.append({
        "x": x,
        "y": y,
        "size": 40,
        "alpha": 255
    })

#health
def draw_health():
    pygame.draw.rect(win, (255, 0, 0), (10, 10, 100, 15))
    pygame.draw.rect(win, (0, 255, 0), (10, 10, player_health, 15))

#game
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    b = bullet_img.get_rect(center=(player.right, player.centery))
                    bullets.append(b)
                    shoot_sound.play()

    #end
    if game_over:
        win.fill((10, 0, 20))

        t = font.render("GAME OVER", True, (255, 0, 0))
        win.blit(t, (W//2 - 90, H//2 - 50))

        s = font.render("Final Score: " + str(score), True, (255, 255, 255))
        win.blit(s, (W//2 - 120, H//2 - 10))

        r = font.render("Press R to Restart", True, (255, 255, 255))
        win.blit(r, (W//2 - 150, H//2 + 30))

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            bullets = []
            enemies = []
            explosions = []
            score = 0
            player_health = 100
            game_over = False

        continue

    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < H:
        player.y += 5

    #e spawn
    spawn_time += 1
    if spawn_time > 40:
        y = random.randint(0, H - 50)
        e = enemy_img.get_rect(topleft=(W, y))
        enemies.append(e)
        spawn_time = 0

    #movement
    for b in bullets:
        b.x += 10

    for e in enemies:
        e.x -= 4

    #hit
    for b in bullets[:]:
        for e in enemies[:]:
            if b.colliderect(e):
                create_explosion(e.x, e.y)
                bullets.remove(b)
                enemies.remove(e)
                explosion_sound.play()
                score += 1
                break

    bullets = [b for b in bullets if b.x < W]
    enemies = [e for e in enemies if e.x > -50]

    #player hit
    for e in enemies[:]:
        if e.colliderect(player):
            player_health -= 25
            create_explosion(e.x, e.y)
            enemies.remove(e)
            explosion_sound.play()

            if player_health <= 0:
                game_over = True

    #explosion
    for ex in explosions[:]:
        ex["size"] += 3
        ex["alpha"] -= 12
        if ex["alpha"] <= 0:
            explosions.remove(ex)

    #draw
    win.blit(bg_img, (0, 0))  

    win.blit(player_img, player)

    for b in bullets:
        win.blit(bullet_img, b)

    for e in enemies:
        win.blit(enemy_img, e)

    #explosion effect
    for ex in explosions:
        surf = pygame.Surface((ex["size"], ex["size"]), pygame.SRCALPHA)
        pygame.draw.circle(
            surf, (255, 200, 50, ex["alpha"]),
            (ex["size"]//2, ex["size"]//2),
            ex["size"]//2
        )
        win.blit(surf, (ex["x"], ex["y"]))

    #points
    score_txt = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_txt, (10, 35))

    draw_health()

    pygame.display.update()

pygame.quit()
