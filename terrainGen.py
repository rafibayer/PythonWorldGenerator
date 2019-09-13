import numpy as np
import noise
import matplotlib.pyplot as plt
import random
import time

# max height for each color
heightToColor = {
        -0.2 : [0, 0, 153], # deep see
        -0.05 : [0, 102, 255], # shallow sea
        0 : [0, 120, 255], # shores
        0.04 : [237, 201, 175], # beach
        0.25 : [96, 128, 56], # grass
        0.3 : [70, 105, 56], # forest
        0.4 : [102, 102, 102], # rocks
        2 : [255, 255, 255] # snow
}

key_list = np.array(list(heightToColor.keys()))
def getColor(height):
        larger_keys = key_list[key_list > height]
        next_key = min(larger_keys)
        return(heightToColor[next_key])

def generateTerrain(width, height, scale, octaves, persistence, lacunarity):
        start = time.time()
        
        colorImage = np.zeros((width, height, 3))
        seed = random.randint(0, 50)

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





