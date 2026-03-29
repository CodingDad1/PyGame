import pygame
import time
import random
pygame.font.init()


#Window adjustmants \/
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")
#\/ Background image
#transform scale will scale your image to the width and height of your game window
BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH,HEIGHT))

#(Player Defined by pixels)
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

#PLayer Velocity (Controls)
PLAYER_VEL = 5


#font - Style and size\/
FONT = pygame.font.SysFont("comicsans", 30)


#Star Defining
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3


#Telling the code to display bg and player \/ Plus elapsed_time
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))

    #Calling the font (f "Text {rounding to nearest second and displaying elapsed time}", AntiAlyasing, "white")
    time_text = FONT.render(f"Time:{round(elapsed_time)} s", 1, "white")
    #Displaying \/ Whats displayed (10p x, 10p y)
    WIN.blit(time_text, (10, 10))

    #drawing stars to apear infront of character when hit.
    for star in stars:
        pygame.draw.rect(WIN, "White", star)

    #\/ player syntax (Window, color, calling player)
    pygame.draw.rect(WIN, (255, 0, 0), player)

    pygame.display.update()

#Main Game Loop \/
def main():
    run = True
#\/ Moving Player (Passing the x position, y position, Width, and Height of our player.)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)


    #optomizing speed for different specs
    clock = pygame.time.Clock()

    #Defining time
    start_time = time.time()
    elapsed_time = 0


    #Projectiles = miliseconds
    star_add_increment = 2000
    star_count = 0

    #storing stars that are currently on screen.
    stars = []
    hit = False


#\/ Running window loop
    while run:
        #FPS Max \/
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        #if count is greater than 2000 miliseconds then add projectiles
        if star_count > star_add_increment:
            for _ in range(3):
                #random star position
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, - STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)



            star_add_increment = max(200, star_add_increment - 500)
            star_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        #Controls\/ (This gives a list of keys the user pressed and records if they were pressed or not)
        keys = pygame.key.get_pressed() 
                                # This creates a border for character to not fly off screen.
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL      #^Same concept but for the right side of the screen.
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL


        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break


        #Ending Screen
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        
        #\/ Make sure to call the Draw function in the loop so it can continue to show up
        draw(player, elapsed_time, stars)    
    pygame.quit()

if __name__ == "__main__":
    main()