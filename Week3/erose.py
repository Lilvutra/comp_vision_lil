# Implementing Erosion(morphological filter)

import cv2
import numpy as np

class Erosion:
    """A class to apply erosion morphological filter to an image."""
    def __init__(self):
        """Initialize the Erosion class."""
        pass

    def apply_erosion(self, img, kernel_size=3, iterations=1):
        """
        Apply erosion filter to the input image.

        Args:
            img: Input image (numpy array).
            kernel_size: Size of the structuring element.
            iterations: Number of times erosion is applied.

        Returns:
            Eroded image.
        """

        if img is None or not isinstance(img, np.ndarray):
            raise ValueError("Input image is invalid")
        if kernel_size <= 0:
            raise ValueError("Kernel size must be a positive integer")
        if iterations <= 0:
            raise ValueError("Iterations must be a positive integer")

        # Create a structuring element
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        # Apply erosion
        eroded_img = cv2.erode(img, kernel, iterations=iterations)
        return eroded_img