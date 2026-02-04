# Implementing dilation(morphological filter)

import cv2
import numpy as np

class Dilation:
    """A class to apply dilation morphological filter to an image."""
    def __init__(self):
        """Initialize the Dilation class."""
        pass

    def apply_dilation(self, img, kernel_size=3, iterations=1):
        """
        Apply dilation filter to the input image.

        Args:
            img: Input image (numpy array).
            kernel_size: Size of the structuring element.
            iterations: Number of times dilation is applied.

        Returns:
            Dilated image.
        """

        if img is None or not isinstance(img, np.ndarray):
            raise ValueError("Input image is invalid")
        if kernel_size <= 0:
            raise ValueError("Kernel size must be a positive integer")
        if iterations <= 0:
            raise ValueError("Iterations must be a positive integer")

        # Create a structuring element
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        # Apply dilation
        dilated_img = cv2.dilate(img, kernel, iterations=iterations)
        return dilated_img