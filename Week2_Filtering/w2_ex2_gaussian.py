import cv2 
import numpy as np

class gaussianFilter:
    """
    Class for applying Gaussian filter to BGR images
    """
    def __init__(self):
        """Initialize Gaussian Filter"""
        pass
    
    def apply_gaussian_filter(self, bgr_img, kernel_size=5):
        """
        Apply Gaussian filter to the BGR image
       
        Args:
            bgr_img: Input image in BGR format (numpy array)
            kernel_size: Size of the Gaussian kernel (must be odd)
            
        Returns:
            Filtered image
        """
        if bgr_img is None or not isinstance(bgr_img, np.ndarray):
            raise ValueError("Input image is invalid")
        if kernel_size % 2 == 0:
            raise ValueError("Kernel size must be an odd number")
        #sigma = 0 means that sigma is calculated based on kernel size
        filtered_img = cv2.GaussianBlur(bgr_img, (kernel_size, kernel_size), 0)
        return filtered_img




















