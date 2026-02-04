import numpy as np
import cv2
import matplotlib.pyplot as plt

Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# read image in bmp format in Captured_Images folder
img = cv2.imread('./Captured_Images/test_grayscale.bmp', cv2.IMREAD_GRAYSCALE)

def convolve(img, kernel):
  m, n = kernel.shape
  y, x = img.shape
  print(f"m, n: {m, n}")
  print(f"y, x: {y, x}")

  out = np.zeros((y, x))
  for i in range(1, y-1):
    for j in range(1, x-1):
      window = img[i-1:i+2, j-1:j+2]
      out[i, j] = np.sum(window * kernel) 
  return out

Ix = convolve(img, Kx)
Iy = convolve(img, Ky)
G = np.sqrt(Ix**2 + Iy**2)
edges = (G > 60).astype(np.uint8) * 255
plt.imshow(edges, cmap='gray')
plt.show()

