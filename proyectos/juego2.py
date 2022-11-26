import os, sys, pygame
def main():
  pygame.init()
  size = width, height = 800, 600
  screen = pygame.display.set_mode(size)
  pygame.display.set_caption("juego pygame")
  while 1: 
    for event in pygame.event.get():
      if event.type == pygame.quit:
        pygame.quit()
        return
if __name__ == "__main__":
  main()