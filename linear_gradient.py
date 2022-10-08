import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

angle = 90 + 90 + 45
sin = np.sin(np.deg2rad(angle))
cos = np.cos(np.deg2rad(angle))

for i, v in enumerate(np.linspace(min(0, sin), max(0, sin), image.shape[0])):
  for i2, v2 in enumerate(np.linspace(min(0, cos), max(0, cos), image.shape[1])):
    t = (abs(v) + abs(v2)) / (abs(sin) + abs(cos))
    
    r = lerp(color1[0], color2[0], t)
    g = lerp(color1[1], color2[1], t)
    b = lerp(color1[2], color2[2], t)
    
    image[i, i2, :] = [r, g, b]
    

plt.figure(1)
plt.imshow(image)
plt.show()
