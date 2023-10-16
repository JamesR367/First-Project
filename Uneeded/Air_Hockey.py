import pygame
import os
pygame.font.init()

pygame.init()
WIDTH, HEIGHT = 900,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Hockey")
SCORE_FONT=pygame.font.SysFont('comicsans',40)
RED =(255,0,0)
BLUE = (0,0,255)
BGC = (234, 212, 252)

FPS = 61
VEL = 5



#All of the Ball items
Ball_Shape= 30
BALL_IMAGE = pygame.image.load(os.path.join('Pictures','Orange.png'))
BALL = pygame.transform.scale(BALL_IMAGE,(Ball_Shape,Ball_Shape))

#All of the paddle items for both left and right
Paddle_Width, Paddle_Height = 20 ,200
PADDLE_IMAGE = pygame.image.load(os.path.join('Pictures','Black.png')) 
LPADDLE = pygame.transform.scale(PADDLE_IMAGE,(Paddle_Width,Paddle_Height))
RPADDLE = pygame.transform.scale(PADDLE_IMAGE,(Paddle_Width,Paddle_Height))
LINE = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)
SQUARE = pygame.Rect(WIDTH//2-25,HEIGHT//2-25,50,50)
MEDIUM_SQUARE = pygame.Rect(WIDTH//2-17.5,HEIGHT//2-17.5,35,35)
SMALL_SQUARE = pygame.Rect(WIDTH//2-5,HEIGHT//2-5,10,10)
 

#Creates the window for the game
def drawWindow(Left,Right,Ball,Lpoint,Rpoint):
    WIN.fill(BGC)
    LScore = SCORE_FONT.render("Score: " + str(Lpoint),1,BLUE)
    RScore = SCORE_FONT.render("Score: " + str(Rpoint),1,BLUE)

    WIN.blit(RScore, ( WIDTH*(2/3),10))
    WIN.blit(LScore, (WIDTH*(1/3)-RScore.get_width(),10))
    pygame.draw.rect(WIN, RED, LINE)
    pygame.draw.rect(WIN, RED, SQUARE)
    pygame.draw.rect(WIN, BGC, MEDIUM_SQUARE)
    pygame.draw.rect(WIN, RED, SMALL_SQUARE)
    WIN.blit(BALL,(Ball.x,Ball.y))
    WIN.blit(LPADDLE,(Left.x,Left.y))
    WIN.blit(RPADDLE,(Right.x,Right.y))
    pygame.display.update()


def Paddle_movement(keys_pressed, Left, Right):
        if keys_pressed[pygame.K_w] and Left.y - VEL > 0-2: #up
            Left.y -= VEL
        if keys_pressed[pygame.K_s]and Left.y + VEL + Paddle_Height < HEIGHT+5: #down
            Left.y += VEL
        if keys_pressed[pygame.K_UP]and Right.y - VEL > 0-2: #up
            Right.y -= VEL
        if keys_pressed[pygame.K_DOWN]and Right.y + VEL + Paddle_Height < HEIGHT+5: #down
            Right.y += VEL
        

def main():
    Lpoint = 0
    Rpoint = 0
    Sidevel = -4
    BaseUpvel = 0
    Upvel = BaseUpvel
    Right = pygame.Rect(WIDTH-Paddle_Width,HEIGHT//2-Paddle_Height//2,Paddle_Width,Paddle_Height)
    Left = pygame.Rect(0,HEIGHT//2-Paddle_Height//2,Paddle_Width,Paddle_Height)
    Ball = pygame.Rect(WIDTH//2-Ball_Shape//2, HEIGHT//2-Ball_Shape//2, Ball_Shape,Ball_Shape)
    clock = pygame.time.Clock()
    run = True
    
    #A loop that runs the game
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()


        #All of this is for the physics for the ball and paddle and 
        #prevents the ball and paddles from going off the screen
        Ball.x += Sidevel
        Ball.top += Upvel
        Lcollide = pygame.Rect.colliderect(Ball,Left)
        Rcollide = pygame.Rect.colliderect(Ball,Right)
        if Lcollide:
            Sidevel *= -1
        if (keys_pressed[pygame.K_w] and Lcollide and Left.y - VEL > 0-2) or (keys_pressed[pygame.K_UP] and Rcollide and Right.y - VEL > 0-2):
            Upvel+= -1
        if (keys_pressed[pygame.K_s] and Lcollide and Left.y + VEL + Paddle_Height < HEIGHT+5) or (keys_pressed[pygame.K_DOWN] and Rcollide and Right.y + VEL + Paddle_Height < HEIGHT+5):
            Upvel+= 1
        if Rcollide:
            Sidevel *= -1
        if Ball.top <= 0:
            Upvel *=-1
        if Ball.bottom >= HEIGHT:
            Upvel *=-1
        if Ball.right >=WIDTH:
            Lpoint +=1
            Ball.x = WIDTH//2-Ball_Shape//2
            Ball.y = HEIGHT//2-Ball_Shape//2
            Upvel = BaseUpvel
        if Ball.left <= 0:
            Rpoint += 1
            Ball.x = WIDTH//2-Ball_Shape//2
            Ball.y = HEIGHT//2-Ball_Shape//2
            Upvel = BaseUpvel

        

        Paddle_movement(keys_pressed,Left,Right)
        drawWindow(Left,Right,Ball,Lpoint,Rpoint)
        
        
    pygame.display.quit()
        
    
    

if __name__=="__main__":
    main()