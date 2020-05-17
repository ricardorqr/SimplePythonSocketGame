import pygame
from network import Network

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')
clientNumber = 0


class Player:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rectangle = (x, y, width, height)
        self.vel = 3

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rectangle)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rectangle = (self.x, self.y, self.width, self.height)


def read_position(string):
    string = string.split(',')
    return int(string[0]), int(string[1])


def make_position(tuple):
    return str(tuple[0]) + ',' + str(tuple[1])


def redraw_window(window, player1, player2):
    window.fill((255, 255, 255))
    player1.draw(window)
    player2.draw(window)
    pygame.display.update()


def main():
    run = True
    network = Network()
    start_prosition = read_position(network.get_position())
    player1 = Player(start_prosition[0], start_prosition[1], 100, 100, (0, 255, 0))
    player2 = Player(0, 0, 100, 100, (255, 0, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        player2_position = read_position(network.send(make_position((player1.x, player1.y))))
        player2.x = player2_position[0]
        player2.y = player2_position[1]
        player2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.move()
        redraw_window(window, player1, player2)


main()
