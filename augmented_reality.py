import cv2
import numpy as np

# Function to apply augmented reality effect
def augmented_reality_effect(image_path, overlay_path):
    image = cv2.imread(image_path)
    overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
    
    # Resize overlay to match the image size
    overlay = cv2.resize(overlay, (image.shape[1], image.shape[0]))
    
    # Split overlay into color and alpha channels
    overlay_color = overlay[:, :, :3]
    overlay_alpha = overlay[:, :, 3] / 255.0
    
    # Apply overlay
    for c in range(0, 3):
        image[:, :, c] = image[:, :, c] * (1 - overlay_alpha) + overlay_color[:, :, c] * overlay_alpha
    
    cv2.imshow('Augmented Reality', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the augmented reality function
if __name__ == "__main__":
    image_path = "path_to_image.jpg"
    overlay_path = "path_to_overlay.png"
    augmented_reality_effect(image_path, overlay_path)
