import time
import cv2
import numpy as np

from Week2_Filtering.w2_ex1_grayscale import GrayscaleConverter
from Week2_Filtering.w2_ex2_gaussian import gaussianFilter
from Week1_Capturing.w1_captureandsave import CaptureAndSave
from Week2_Filtering.w2_ex3_medianblur import MedianBlurFilter

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
        
        results = {}
        
        saveImg = CaptureAndSave()
        
        step1_image = saveImg.save_image(bgr_img, "test_capture.bmp")
        
        # Convert to grayscale, refering to Week2_Filtering/w2_ex1_grayscale.py
        
        grayConverter = GrayscaleConverter()
        step2_img = grayConverter.convert_to_grayscale(step1_image)

        #medianBlur = MedianBlurFilter()
        gaussianFilterObj = gaussianFilter()
        
        #processed_img = medianBlur.apply_median_blur(processed_img, kernel_size=5)
        step3_img = gaussianFilterObj.apply_gaussian_filter(step2_img, kernel_size=5)   
        #step3_image = saveImg.save_image(processed_img, "test_grayscale.bmp")
        #step3_image = saveImg.save_image(processed_img, "test_medianblur.bmp")
        processed_img = saveImg.save_image(step3_img, "test_gaussianblur.bmp")

        process_time_ms = (time.perf_counter() - start_time) * 1000

        return processed_img, results, process_time_ms
    
    def visualize_results(self, bgr_img, results):
        """
        Visualize the results of image processing
       
        Args:
            bgr_img: Input image in BGR format
            results: Dictionary containing processing results
        Returns:
            Annotated image
        """
        # TODO: Implement visualization logic
        pass

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
