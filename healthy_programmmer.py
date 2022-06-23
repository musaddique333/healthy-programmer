import time
import pygame


# def


if __name__ == '__main__':
    #Water related
    w_m = pygame.mixer.Sound("")
    w_t = time.time()
    print("drink water")
    while True:
        w_temp = time.time()
        if w_temp == w_t + 5:
            print("after 5")
            w_t += 5




