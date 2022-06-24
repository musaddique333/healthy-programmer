import time
import pygame
import numpy as np


def task_done(music, file_name, message):
    music.play(-1)
    print(message)
    with open(f"{file_name}", "a") as f:
        f.write(f"reminded at {time.ctime()}\n")
    done_work = input()
    music.stop()
    with open(f"{file_name}", "a") as f:
        f.write(f"\t{done_work} at {time.ctime()}\n\n")


if __name__ == '__main__':
    pygame.mixer.init()
    water_music = pygame.mixer.Sound("audio/water.mp3")
    eyes_music = pygame.mixer.Sound("audio/eyes.mp3")
    exercise_music = pygame.mixer.Sound("audio/exercise.mp3")

    exercise_array1 = np.array([9.45, 10.3, 11.15, 12.0, 12.45, 13.3, 14.15, 15.0, 15.45, 16.3, 17.15, 18.0, 18.45, 19.3, 20.15, 21.0, 21.45, 22.3, 23.15, 0.0, 0.45, 1.3, 2.15, 3.0, 3.45, 4.3, 5.15, 6.0, 6.45, 7.3, 8.15, 9.0])
    exercise_array2 = np.array([12.0, 15.0, 18.0, 21.0, 0.0, 3.0, 6.0, 9.0])
    c1, c2, c3, c4, c5 = 0, 0, 0, 0, 0
    while True:
        eyes = time.ctime().split()
        water = time.ctime().split()
        exercise = time.ctime().split()

        eyes = eyes[3].split(":")
        water = water[3].split(":")
        exercise = exercise[3].split(":")

        eyes = int(eyes[1])
        water = int(water[1])
        exercise.pop()
        exercise = float(f"{exercise[0]}.{exercise[1]}")

        if water == 0 and eyes == 0 and exercise in exercise_array2:
            if c1 == 0:
                c1 = 1
                c2, c3, c4, c5 = 0, 0, 0, 0
                task_done(water_music, "water.txt", "Say Drank if done drinking")
                task_done(eyes_music, "eyes.txt", "Say Eyes done if done with eyes exercise")
                task_done(exercise_music, "exercise.txt", "Say Exercise done is done with exercise")

        elif water == 0 and eyes == 0:
            if c2 == 0:
                c2 = 1
                c1, c3, c4, c5 = 0, 0, 0, 0
                task_done(water_music, "water.txt", "Say Drank if done drinking")
                task_done(eyes_music, "eyes.txt", "Say Eyes done if done with eyes exercise")

        elif water == 0:
            if c3 == 0:
                c3 = 1
                c1, c2, c4, c5 = 0, 0, 0, 0
                task_done(water_music, "water.txt", "Say Drank if done drinking")

        elif eyes == 0 or eyes == 30:
            if c4 == 0:
                c4 = 1
                c1, c2, c3, c5 = 0, 0, 0, 0
                task_done(eyes_music, "eyes.txt", "Say Eyes done if done with eyes exercise")

        elif exercise in exercise_array1:
            if c5 == 0:
                c5 = 1
                c1, c2, c3, c4 = 0, 0, 0, 0
                task_done(exercise_music, "exercise.txt", "Say Exercise done is done with exercise")
