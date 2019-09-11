import numpy as np
import noise
import matplotlib.pyplot as plt
import random

# max height for each color
heightToColor = {
        -0.25 : [0, 0, 153], # deep see
        -0 : [0, 102, 255], # shallow sea
        0.1 : [237, 201, 175], # beach
        0.2 : [96, 128, 56], # grass
        0.35 : [102, 102, 102], # rocks
        1 : [255, 255, 255] # snow
}

def generateNoise(width, height, scale, octaves, persistence, lacunarity):
        pn = np.zeros((width, height))

        seed = random.randint(0, 50)

        for x in range(width):
                for y in range(height):
                        pn[x,y] = noise.pnoise2(x/scale, y/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, 
                        base = seed)

        
        return pn
        
def generateTerrain(width, height, scale, octaves, persistence, lacunarity):
        noise = generateNoise(width, height, scale, octaves, persistence, lacunarity)
        colorImage = np.zeros((noise.shape[0], noise.shape[1], 3))

        for x in range(width):
                for y in range(height):
                        colorImage[x, y] = getColor(noise[x, y])

        return colorImage.astype('uint8')

def getColor(height):
        key_list = np.array(list(heightToColor.keys()))
        larger_keys = key_list[key_list > height]
        next_key = min(larger_keys)
        return(heightToColor[next_key])

