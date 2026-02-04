# Implementing Laplacian edge detection filter

import cv2
import numpy as np

class LaplacianFilter:
    
    """A class to apply Laplacian edge detection filter on images."""
    def __init__(self):
        """Initialize the LaplacianFilter class."""
        pass

    def apply_laplacian(self, image, ksize=3):
        """
        Apply Laplacian filter to the input image.

        Args:
            image: Input image (numpy array).
            ksize: Kernel size for the Laplacian filter (must be odd).

        Returns:
            Filtered image.
        """

        if image is None or not isinstance(image, np.ndarray):
            raise ValueError("Input image is invalid")
        if ksize % 2 == 0:
            raise ValueError("Kernel size must be an odd number")

        laplacian_img = cv2.Laplacian(image, cv2.CV_64F, ksize=ksize)
        return laplacian_img
















