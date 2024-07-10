import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Ensure TensorFlow uses the GPU
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
    except:
        pass

# Example function to generate an image using a GAN model
def generate_image():
    # Load a pre-trained GAN model (for example, DCGAN)
    model = tf.keras.models.load_model('path_to_gan_model')
    
    # Generate random noise
    noise = np.random.normal(0, 1, (1, 100))
    
    # Generate an image
    generated_image = model.predict(noise)
    
    # Plot the generated image
    plt.imshow((generated_image[0] * 127.5 + 127.5).astype(np.uint8))
    plt.axis('off')
    plt.show()

# Test the image generation function
if __name__ == "__main__":
    generate_image()
