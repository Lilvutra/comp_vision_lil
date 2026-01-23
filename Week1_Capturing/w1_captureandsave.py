import cv2 
import os
import numpy as np

class CaptureAndSave():
    """
    Class for capturing images from camera and saving them to disk
    """
    def __init__(self):
        """Initialize capture and save"""
        pass
    
    def save_image(self, bgr_img, filename):
        """
        Save the BGR image to disk with the given filename
        
        Args:
            bgr_img: Input image in BGR format (numpy array)
            filename: Filename to save the image
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        if bgr_img is None or not isinstance(bgr_img, np.ndarray):
            print("No image to save.")
            return False
        
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            # Save the image
            cv2.imwrite(filename, bgr_img)
            print(f"Image saved to {filename}")
            return True
        
        except Exception as e:
            print(f"Failed to save image: {e}")
            return False
    
    
   