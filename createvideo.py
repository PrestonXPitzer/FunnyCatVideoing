import pygame
from RTP import openAudioStream, getCurrrentAudioIntensity
import time


def main():
    #create a new audio stream
    stream = openAudioStream()
    #init pygame
    pygame.init()
    #set the screen size
    screen = pygame.display.set_mode((2560, 1080))
    images = ["cat\\" + str(i) + ".png" for i in range(1, 24)]
    smallest = 10000000000
    largest = 0
    while (True):
        intensity = getCurrrentAudioIntensity(stream)  
        calculatedIntensity = 0
        #display the appropriate image based on the intensity
        if intensity < smallest:
            smallest = intensity
        if intensity > largest:
            largest = intensity
        #split the range between smallest and largest into 23 parts, and then map the intensity to the corresponding image
        if (largest - smallest) == 0:
            calculatedIntensity = 0
        else:
            calculatedIntensity = int(((intensity - smallest) / (largest - smallest)) * 23)
        print(calculatedIntensity)
        if calculatedIntensity == 23:
            calculatedIntensity = 22
        screen.blit(pygame.image.load(images[calculatedIntensity]), (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
