import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
    slika = slika.astype(np.float32)

    height, width = slika.shape[:2]
    new_height = height + 2
    new_width = width + 2

    # novo polje samih ničel
    new_image = np.zeros((new_height, new_width), dtype=np.float32)

    # kopiramo v sredino polja tako da imamo rob ničel
    new_image[1:new_height - 1, 1:new_width - 1] = slika

    # naredimo začasno polje, ki ga bomo vrnili
    output_image = np.zeros_like(slika, dtype=np.float32)

    for y in range(0,height):
        for x in range(0,width):
            # Get window around current pixel

            window = new_image[y:y + 3, x:x + 3]

            # Apply convolution operation
            output_image[y, x] = np.sum(window * jedro)

    output_image = np.clip(output_image, 0, 255)  # Clip values to [0, 255]
    output_image = output_image.astype(np.uint8)  # Convert back to uint8
    return output_image
    pass
    pass

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    pass

def filtriraj_sobel_smer(slika):

    pass

    return slika
    pass

if __name__ == '__main__':
img = cv.imread(".utils/lenna.png",cv.IMREAD_GRAYSCALE)
    jedro = np.array([[1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9],
                      [1/9, 1/9,1/9]], dtype=np.float32)
    imgTest=konvolucija(img,jedro)
    pass
