import numpy as np
from matplotlib import pyplot as plt
from skimage.measure import regionprops, label
from skimage.morphology import erosion, dilation

def count_lakes_and_bays(region):
  symbol = ~region.image  # инвертируем и делаем маркировку, чтобы определить области озера и залива
  labels = label(symbol)
  lakes = 0
  bays = 0
  for reg in regionprops(labels):
    flag = True
    for y, x in reg.coords:
      if (y == 0 or x == 0 or y == region.image.shape[0]-1 or x == region.image.shape[1]-1):
        flag = False
        break
    lakes += flag
    bays += not flag
  return lakes, bays

def has_vline(image):
  return 1 in erosion(np.mean(image, 0), [1, 1, 1])

def has_hline(image):
  return 1 in np.mean(image, 1)

def recognize(image_region):
  lakes, bays = count_lakes_and_bays(image_region)
  if lakes == 2:  # B or 8
    if has_vline(image_region.image):
      return 'B'
    else:
      return '8'
  elif lakes == 1: # A or 0
    if bays == 4:
      return '0'
    elif bays == 3:
      return 'A'
    else:
      if image_region.eccentricity > 0.65:
        return 'P'
      else:
        return 'D'
  elif lakes == 0:
    if np.mean(image_region.image) == 1.0:
      return '-'
    elif has_vline(image_region.image):
      return '1'
    elif bays == 2:
      return '/'
    elif has_hline(image_region.image):
      return '*'
    elif bays == 4:
      return 'X'
    else:
      return 'W'
image = plt.imread("symbols.png")
image = np.mean(image, 2)  # избавляемся от цвета по среднему
image[image > 0] = 1  # бинаризируем

labels = label(image)  # label норм работает только для бинарных изображений

regions = regionprops(labels) # здесь находятся все символы
result = {}

print('% of letters: ')
for reg in regions:
  symbol = recognize(reg)
  if symbol not in result:
    result[symbol] = 0
  result[symbol] += 1 / 400 * 100
print(result)
print('\n% sum: ', sum(result.values()))

# print(count_lakes_and_bays(regions[51]))
# plt.imshow(regions[7].image)
# plt.show()