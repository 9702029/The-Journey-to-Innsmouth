import pygame

pygame.init()
display_width = 1280
display_height = 720
display_time = 5000
x = 2
y = 2
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
testImage = pygame.image.load("investigatorOffice.png").convert()
surface1 = pygame.Surface((display_width, display_height))


def draw_image1(testImage, x, y, display_time):
  running = True
  display_width = 1000
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_testimage = pygame.transform.scale(
      testImage, (testImage.get_width() // 1.2, testImage.get_height() // 1.2))
  while running:
    screen.blit(scaled_testimage, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    # displayTime = clock.tick(60) / 1000


image2 = pygame.image.load("gamestart.png").convert_alpha()
scaled_image2 = pygame.transform.scale(image2, (1, 1))


def draw_image2(image2, x, y):
  running = True
  display_width = 1280
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  display_time = 5000
  scaled_image2 = pygame.transform.scale(
      image2, (image2.get_width() // 1.5, image2.get_height() // 1.5))
  while running:
    screen.blit(scaled_image2, (x, y))
    pygame.display.flip()
    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    #displayTime = clock.tick(60) / 1000


image3 = pygame.image.load("Drawing(1).png").convert_alpha()
scaled_image3 = pygame.transform.scale(image3, (1, 1))


def draw_image3(image3, x, y):
  running = True
  display_width = 1280
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  display_time = 5000
  scaled_image3 = pygame.transform.scale(
      image3, (image3.get_width() // 1, image3.get_height() // 1))
  while running:
    screen.blit(scaled_image3, (x, y))
    pygame.display.flip()
    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    #displayTime = clock.tick(60) / 1000
