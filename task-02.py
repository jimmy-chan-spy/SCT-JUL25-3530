from PIL import Image
import numpy as np

def load_image(path):
    image = Image.open(path)
    return image.convert("RGB")

def save_image(image_array, path):
    encrypted_image = Image.fromarray(image_array.astype('uint8'))
    encrypted_image.save(path)

def swap_pixels(image_array):
   
    return np.fliplr(image_array)

def invert_pixels(image_array):
   
    return 255 - image_array

def encrypt_image(path, output_path, mode="swap"):
    image = load_image(path)
    image_array = np.array(image)

    if mode == "swap":
        encrypted_array = swap_pixels(image_array)
    elif mode == "invert":
        encrypted_array = invert_pixels(image_array)
    else:
        raise ValueError("Unsupported encryption mode")

    save_image(encrypted_array, output_path)
    print(f"Encrypted image saved to {output_path}")

