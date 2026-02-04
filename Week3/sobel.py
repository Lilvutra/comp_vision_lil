# Implementing sobel edge detection filter
import cv2
import numpy as np

class SobelEdgeDetector:
    """
    Class for applying Sobel edge detection filter to BGR images
    """
    def __init__(self):
        """Initialize Sobel Edge Detector"""
        pass
    
    def apply_sobel_filter(self, bgr_img, kernel_size=5):
        """
        Apply Sobel filter to the BGR image
       
        Args:
            bgr_img: Input image in BGR format (numpy array)
            kernel_size: Size of the Sobel kernel (must be odd)
            
        Returns:
            Filtered image
        """
        if bgr_img is None or not isinstance(bgr_img, np.ndarray):
            raise ValueError("Input image is invalid")
        if kernel_size % 2 == 0:
            raise ValueError("Kernel size must be an odd number")
        
        filtered_img = cv2.Sobel(bgr_img, cv2.CV_64F, 1, 1, ksize=kernel_size)
        return filtered_img

