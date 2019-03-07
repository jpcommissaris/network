import pygame

# -- colors --
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

pygame.init()
width = 400
height = 500

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("A client")

clientNumber = 0
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -- objects --
class Player():
    def __init__(self,x,y,width,height,color):
        self.x=x; self.y=y; self.height= height; self.width = width;
        self.color = color
        self.rect = (x,y,width,height)
        self.v = 3

    def draw(s,win):
        pygame.draw.rect(win,s.color,s.rect)
    def move(s):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            s.x -= s.v
        if keys[pygame.K_RIGHT]:
            s.x += s.v
        if keys[pygame.K_UP]:
            s.y -= s.v
        if keys[pygame.K_DOWN]:
            s.y += s.v
        
        s.rect = (s.x,s.y,s.width,s.height)


# -- main functions --
def drawWindow(win,player):
    # --- new drawings ---
    player.draw(win)



# -- game loop --
def main():
    run = True
    p = Player(50,50,100,100,GREEN, )

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        # -- updates objects --
        p.move()

        # -- updates drawings --
        screen.fill(WHITE)
        drawWindow(screen,p)
        pygame.display.flip()
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()

main()


