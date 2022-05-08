from pygame.locals import *
import pygame
import time

# Player class
class Player:
    # Horizontal position
    x = 0

    # Vertical position
    y = 0

    # Snake direction
    d = 0

    # Old positions
    positions = []

    # Max length of snake
    length = 3

class Game:
    def __init__(self):
        self._running = True

        # Create snake player
        self.player = Player()

    def on_init(self):
        # Initialize pygame
        pygame.init()

        # Create window
        self._display_surf = pygame.display.set_mode((640,480), pygame.HWSURFACE)

        # Set window title
        pygame.display.set_caption('Pygame example')

        # Load image
        self._lion_image = pygame.image.load("lion.png").convert()

    def on_render(self):
        # Clear screen
        self._display_surf.fill((0,0,0))
        #self._display_surf.blit(self._lion_image, (self.player.x,self.player.y))

        # Draw snake
        for pos in self.player.positions:
            self._display_surf.blit(self._lion_image, (pos[0],pos[1]))

        # Update screen
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            # Keyboard input
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.d = 0

            if keys[K_LEFT]:
                self.player.d = 1

            if keys[K_UP]:
                self.player.d = 2

            if keys[K_DOWN]:
                self.player.d = 3

            # Update current position based on direction
            if self.player.d == 0:
                self.player.x += 44
            elif self.player.d == 1:
                self.player.x -= 44
            elif self.player.d == 2:
                self.player.y -= 44
            elif self.player.d == 3:
                self.player.y += 44

            # Increase snake length
            if len(self.player.positions) < self.player.length:
                self.player.positions.append((self.player.x,self.player.y))
            else:
                self.player.positions.pop(0)
                self.player.positions.append((self.player.x,self.player.y))


            # Update screen
            self.on_render()
            time.sleep(0.1)

        self.on_cleanup()

if __name__ == "__main__" :
    game = Game()
    game.on_execute()
