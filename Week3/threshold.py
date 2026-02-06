# Implementing thresholding(binary)

import cv2
import numpy as np

class Threshold:
    """A class to apply binary thresholding to an image."""
    def __init__(self):
        """Initialize the Threshold class."""
        pass

    def apply_threshold(self, img, thresh=127, max_value=255):
        """
        Apply binary thresholding to the input image.

        Args:
            img: Input image (numpy array).
            thresh: Threshold value.
            max_value: Maximum value to use with the THRESH_BINARY thresholding.

        Returns:
            Thresholded image.
        """

        if img is None or not isinstance(img, np.ndarray):
            raise ValueError("Input image is invalid")
        if not (0 <= thresh <= 255):
            raise ValueError("Threshold must be in the range [0, 255]")
        if not (0 <= max_value <= 255):
            raise ValueError("Max value must be in the range [0, 255]")

        # Apply binary thresholding
        _, thresholded_img = cv2.threshold(img, thresh, max_value, cv2.THRESH_BINARY)
        return thresholded_img