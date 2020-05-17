import pygame
from network import Network


class Client:

    def __init__(self, client_number, width=500, height=500):
        self.client_number = client_number
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Client ' + str(client_number))

    def __redraw_window(self, window, player1, player2):
        window.fill((255, 255, 255))
        player1.draw(window)
        player2.draw(window)
        pygame.display.update()

    def run(self):
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
            self.__redraw_window(self.window, player1, player2)


if __name__ == "__main__":
    client1 = Client(1)
    client1.run()

    # client2 = Client(2)
    # client2.run()
