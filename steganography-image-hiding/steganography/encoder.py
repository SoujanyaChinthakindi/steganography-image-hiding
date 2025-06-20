# encoder.py
# Sample encoder script using LSB

def encode_image(image_path, message, output_path):
    from PIL import Image
    import numpy as np

    img = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # EOF marker
    data = np.array(img)
    flat_data = data.flatten()

    for i in range(len(binary_message)):
        flat_data[i] = (flat_data[i] & ~1) | int(binary_message[i])

    encoded_data = flat_data.reshape(data.shape)
    encoded_img = Image.fromarray(encoded_data.astype('uint8'))
    encoded_img.save(output_path)
