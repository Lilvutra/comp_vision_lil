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
            save_dir = "Captured_Images"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            # Save the image
            save_path = os.path.join(save_dir, filename)
            cv2.imwrite(save_path, bgr_img)
            print(f"Image saved to {save_path}")
            return True
        
        except Exception as e:
            print(f"Failed to save image: {e}")
            return False
   
    
   