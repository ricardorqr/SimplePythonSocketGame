import pygame
from network import Network


width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')


def redraw_window(window, player1, player2):
    window.fill((255, 255, 255))
    player1.draw(window)
    player2.draw(window)
    pygame.display.update()


def main():
    run = True
    network = Network()
    player1 = network.get_player()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        player2 = network.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.move()
        redraw_window(window, player1, player2)


main()
