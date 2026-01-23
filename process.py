import time
import cv2
import numpy as np
from Week2_Filtering.w2_ex2_gaussian import gaussianFilter
from Week1_Capturing.w1_captureandsave import CaptureAndSave

class ImageProcessor:
    """
    Class for processing images from camera feed
    """
    frame = None  # BGR numpy array
    def __init__(self, frame=None):
        """Initialize image processor"""
        self.frame = frame
        pass
    
    def process_frame(self, bgr_img):
        """
        Process a single frame
        
        Args:
            bgr_img: Input image in BGR format (numpy array)
            
        Returns:
            tuple: (Processed image, process time in ms)
        """
        if bgr_img is None:
            raise ValueError("Input frame is None")

        start_time = time.perf_counter()

        h, w = bgr_img.shape[:2]
        side = int(min(h, w) * 0.5)
        cx, cy = w // 2, h // 2
        x0 = max(0, cx - side // 2)
        y0 = max(0, cy - side // 2)
        crop = bgr_img[y0:y0+side, x0:x0+side].copy()

        processed = cv2.resize(crop, (256, 256))

        process_time_ms = (time.perf_counter() - start_time) * 1000

        return processed, process_time_ms
    
    # WEEK1: Image Processing Filters 
    def convert_to_grayscale(self, bgr_img):
        """
        Convert BGR image to Grayscale
        
        Args:
            bgr_img: Input image in BGR format
            
        Returns:
            Grayscale image
        """
        start = time.perf_counter()

        gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
        process_time = (time.perf_counter() - start) * 1000

        return gray_img, process_time
    def gaussian_filter(self, bgr_img, kernel_size=5):
        """
        Apply Gaussian filter to the image
        
        Args:
            bgr_img: Input image in BGR format
            kernel_size: Size of the Gaussian kernel
            
        Returns:
            Filtered image
        """
        start = time.perf_counter()

        filtered_img = cv2.GaussianBlur(bgr_img, (kernel_size, kernel_size), 0)
        process_time = (time.perf_counter() - start) * 1000

        return filtered_img, process_time
    
    def preprocess(self, bgr_img):
        """
        Preprocess image (e.g., resize, normalize)
        
        Args:
            bgr_img: Input image in BGR format
            
        Returns:
            Preprocessed image
        """
        # TODO: Implement preprocessing
        pass
    
    def postprocess(self, result):
        """
        Postprocess results
        
        Args:
            result: Processed result
            
        Returns:
            Postprocessed result
        """
        # TODO: Implement postprocessing
        pass
