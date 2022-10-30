import numpy as np
from matplotlib import pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_erosion

image = np.load('ps.npy.txt')

labels = label(image)
print('Кол-во объектов на изображении: ', np.amax(labels))

footprint_full = [[1, 1, 1, 1, 1], 
                  [1, 1, 1, 1, 1], 
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1]]

eros = binary_erosion(image, footprint_full)
labels = label(eros)
quantity_full = np.amax(labels)
print(f'Сумма горизонтальных целых прямоугольников: {quantity_full}')

footprint_top = [[1, 0, 0, 0, 1], 
                 [1, 0, 0, 0, 1], 
                 [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1]]

eros = binary_erosion(image, footprint_top)
labels = label(eros)
quantity_top = np.amax(labels) - quantity_full
print(f'Сумма горизонтальных прямоугольников с вырезом сверху: {quantity_top}')

footprint_bottom = [[1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1], 
                    [1, 0, 0, 0, 1, 1],
                    [1, 0, 0, 0, 1, 1]]

eros = binary_erosion(image, footprint_bottom)
labels = label(eros)
quantity_bottom = np.amax(labels) - quantity_full
print(
  f'Сумма горизонтальных прямоугольников с вырезом снизу: {quantity_bottom}')

footprint_left = [[1, 1, 1, 1], 
                  [0, 0, 1, 1], 
                  [0, 0, 1, 1], 
                  [0, 0, 1, 1],
                  [1, 1, 1, 1]]

eros = binary_erosion(image, footprint_left)
labels = label(eros)
quantity_left = np.amax(labels)
print(f'Сумма вертикальных прямоугольников с вырезом слева: {quantity_left}')

footprint_right = [[1, 1, 1, 1], 
                   [1, 1, 0, 0], 
                   [1, 1, 0, 0], 
                   [1, 1, 0, 0],
                   [1, 1, 1, 1]]

eros = binary_erosion(image, footprint_right)
labels = label(eros)
quantity_right = np.amax(labels)
print(f'Сумма вертикальных прямоугольников с вырезом справа: {quantity_right}')

quantity_of_all_objects = quantity_full + quantity_top + quantity_bottom + quantity_left + quantity_right
print(f'Сумма всех объектов: {quantity_of_all_objects}')

plt.imshow(image)
plt.show()
