import time
import cv2
import numpy as np

from Week2_Filtering.w2_ex1_grayscale import GrayscaleConverter
from Week2_Filtering.w2_ex2_gaussian import gaussianFilter
from Week1_Capturing.w1_captureandsave import CaptureAndSave
from Week2_Filtering.w2_ex3_medianblur import MedianBlurFilter
from Week3.sobel import SobelEdgeDetector
from Week3.laplacian import LaplacianFilter
from Week3.sharpen import Sharpen
from Week3.bilateral import BilateralFilter
from Week3.threshold import Threshold
from Week3.erose import Erosion
from Week3.dilate import Dilation

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
        
        # Capture and save original image 
        saveImg = CaptureAndSave()
        
        step1_image = saveImg.save_image(bgr_img, "test_capture.bmp")
        
        # This pipeline currently just support one filter at a time
        
        # Convert to grayscale, refering to Week2_Filtering/w2_ex1_grayscale.py
        #grayConverter = GrayscaleConverter()
        #processed_img = grayConverter.convert_to_grayscale(bgr_img)

        #medianBlur = MedianBlurFilter()
        #processed_img = medianBlur.apply_median_blur(processed_img, kernel_size=5)

        # Gaussian filter, refering to Week2_Filtering/w2_ex2_gaussian.py
        #gaussianFilterObj = gaussianFilter()
        #processed_img = gaussianFilterObj.apply_gaussian_filter(bgr_img, kernel_size=5)   
       
        # Sobel edge detection, refering to Week3/sobel.py
        #sobelDetector = SobelEdgeDetector()
        #processed_img = sobelDetector.apply_sobel_filter(bgr_img, kernel_size=5)
       
        # Laplacian filter, refering to Week3/laplacian.py
        #laplacianFilter = LaplacianFilter()
        #processed_img = laplacianFilter.apply_laplacian(bgr_img)
        
        # Sharpening
        #sharpenFilter = Sharpen()
        #processed_img = sharpenFilter.apply_sharpen(bgr_img)
        
        # Bilateral, later try with different parameters
        #bilateral = BilateralFilter()
        #processed_img = bilateral.apply_bilateral(bgr_img)
        
        # Thresholding
        #threshold = Threshold()
        #processed_img = threshold.apply_threshold(bgr_img)
        
        # Erosion
        #ero = Erosion()
        #processed_img = ero.apply_erosion(bgr_img)
        
        
        # Dilation
        dilala = Dilation()
        processed_img = dilala.apply_dilation(bgr_img)
        
        step3_img = saveImg.save_image(processed_img, "test_s.bmp")

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
