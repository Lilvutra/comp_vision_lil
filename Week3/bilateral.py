# Implementing bilateral filter

import cv2
import numpy as np

class BilateralFilter:
    """A class to apply bilateral filter to an image."""
    def __init__(self):
        """Initialize the BilateralFilter class."""
        pass

    def apply_bilateral(self, img, d=9, sigma_color=75, sigma_space=75):
        """
        Apply bilateral filter to the input image.

        Args:
            img: Input image (numpy array).
            d: Diameter of each pixel neighborhood.
            sigma_color: Filter sigma in color space.
            sigma_space: Filter sigma in coordinate space.

        Returns:
            Filtered image.
        """

        if img is None or not isinstance(img, np.ndarray):
            raise ValueError("Input image is invalid")
        if d <= 0:
            raise ValueError("Diameter must be a positive integer")
        if sigma_color <= 0:
            raise ValueError("Sigma color must be a positive number")
        if sigma_space <= 0:
            raise ValueError("Sigma space must be a positive number")

        # Apply bilateral filter
        bilateral_img = cv2.bilateralFilter(img, d, sigma_color, sigma_space)
        return bilateral_img
    
    