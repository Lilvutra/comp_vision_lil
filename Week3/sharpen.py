# Implementing Sharpening filter

class Sharpen:
    """A class to apply a sharpening filter to an image."""
    def __init__(self):
        """Initialize the Sharpen class."""
        pass
    def apply_sharpen(self, img):
        """
        Apply a sharpening filter to the input image.

        Args:
            img: Input image in BGR format (numpy array)

        Returns:
            Sharpened image
        """
        import cv2
        import numpy as np

        if img is None or not isinstance(img, np.ndarray):
            raise ValueError("Input image is invalid")

        # Define a sharpening kernel
        kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])

        # Apply the sharpening kernel to the image
        sharpened_img = cv2.filter2D(img, -1, kernel)
        return sharpened_img