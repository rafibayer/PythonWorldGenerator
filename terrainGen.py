import numpy as np
import noise
import matplotlib.pyplot as plt
import random
import time

# max height for each color
htc = None
key_list = None

# gets the color for the next height key > height
def getColor(height):
        larger_keys = key_list[key_list > height]
        next_key = min(larger_keys)
        return(htc[next_key])

# generates a color terrain with a height to color dictionary specifying how to color different heights
# also takes width, height, scale, octaves, persistence, and lacunarity parameters to generate noise
def generateTerrain(heightToColorDict, width, height, scale, octaves, persistence, lacunarity):
        start = time.time()

        # store height to color dict and keys as global variables
        global htc
        htc = heightToColorDict
        global key_list
        key_list = np.array(sorted(list(heightToColorDict.keys())))
        
        # blank color image
        colorImage = np.zeros((width, height, 3))
        seed = random.randint(0, 50)

        # generate noise and pick corresponding value for every x and y in with and height
        for x in range(width):
                for y in range(height):
                        colorImage[x,y] = getColor( 
                                noise.pnoise2(
                                        x/scale, 
                                        y/scale, 
                                        octaves=octaves, 
                                        persistence=persistence,
                                        lacunarity=lacunarity, 
                                        base = seed
                                )
                        )

        print(f"took {time.time() - start} to generate terrain")
        return colorImage.astype('uint8')





