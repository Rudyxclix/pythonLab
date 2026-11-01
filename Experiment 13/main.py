import numpy as np

pixels = np.array([0, 10, 20, 30, 40, 50, 60, 70,
                   80, 90, 100, 110, 120, 130, 140, 150])
image = pixels.reshape(4, 4)
print("Image matrix:")
print(image)

region = image[1:3, 1:3]
print("Selected 2x2 region:")
print(region)

bright_image = np.clip(image + 10, 0, 255)
print("Image after increasing brightness by 10:")
print(bright_image)

transform = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
])
transformed_image = image @ transform
print("Image after swapping the last two columns with matrix multiplication:")
print(transformed_image)
