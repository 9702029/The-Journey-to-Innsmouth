import pygame
pygame.init()
display_width = 400
display_height = 400
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
testImage = pygame.image.load("test1.png")
def draw_test_image(x, y, running=True):
        while running:
            screen.blit(testImage, (x, y))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            dt = clock.tick(60) / 1000
        pygame.quit()