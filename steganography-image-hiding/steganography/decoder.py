# decoder.py
# Sample decoder script using LSB

def decode_image(image_path):
    from PIL import Image
    import numpy as np

    img = Image.open(image_path)
    data = np.array(img).flatten()
    bits = [str(data[i] & 1) for i in range(len(data))]
    chars = [chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars)
    return message.split('ÿÿÿÿÿÿÿÿÿÿÿÿÿÿ')[0]
