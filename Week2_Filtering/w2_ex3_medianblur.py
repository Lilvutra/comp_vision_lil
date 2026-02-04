import cv2
import numpy as np

class MedianBlurFilter:
    """
    Class for applying Median Blur filter to BGR images
    """
    def __init__(self):
        """Initialize Median Blur Filter"""
        pass
  
    def apply_median_blur(self, bgr_img, kernel_size=5):
        """
        Apply Median Blur filter to the BGR image
        
        Args:
            bgr_img: Input image in BGR format (numpy array)
            kernel_size: Size of the median kernel (must be odd)
            
        Returns:
            Filtered image
        """
        if bgr_img is None or not isinstance(bgr_img, np.ndarray):
            raise ValueError("Input image is invalid")
        if kernel_size % 2 == 0:
            raise ValueError("Kernel size must be an odd number")
        
        filtered_img = cv2.medianBlur(bgr_img, kernel_size)
        return filtered_img