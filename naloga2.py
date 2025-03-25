import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
'''Izvede konvolucijo nad sliko. Brez uporabe funkcije cv.filter2D, ali katerekoli druge funkcije, ki izvaja konvolucijo.
    Funkcijo implementirajte sami z uporabo zank oz. vektorskega računanja.'''
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
    '''Filtrira sliko z Gaussovim jedrom..'''
    velikost_jedra = int((2*sigma)*2+1)
    k = (velikost_jedra/2)-(1/2)

    kernel = np.fromfunction(lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * np.exp(
        -((x - k - 1) ** 2 + (y - k - 1) ** 2) / (2 * sigma ** 2)),
                             (velikost_jedra, velikost_jedra))

    # Apply convolution with Gaussian kernel
    slika = konvolucija(slika, jedro)

    return slika
    pass

def filtriraj_sobel_smer(slika):
     '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''


    sobel_y = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    slika = cv.filter2D(slika, -1, sobel_y)

    height, width = slika.shape[:2]
    temp_img = np.zeros((slika.shape[0], slika.shape[1], 3), dtype=np.float32)

    # Find indices where pixel values are higher than 120
    for y in range(0, slika.shape[0], 1):
        for x in range(0, slika.shape[1], 1):
            if slika[y, x] > 120:
                temp_img[y, x] = [255, 0, 0]

    return temp_img

    return slika
    pass

    return slika
    pass

if __name__ == '__main__':
img = cv.imread(".utils/lenna.png",cv.IMREAD_GRAYSCALE)
    jedro = np.array([[1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9],
                      [1/9, 1/9,1/9]], dtype=np.float32)
                      sigma = 1.5
    cv.imshow("navadna", img)
    imgTest = filtriraj_sobel_smer(img)
    cv.imshow("Sobel", imgTest)
    cv.waitKey(0)
    
     imgTest = filtriraj_z_gaussovim_jedrom(img, sigma)
    cv.imshow("Gaussov Filter", imgTest)

    cv.waitKey(0)
    
    imgTest=konvolucija(img,jedro)
    cv.imshow("Navdna Konvulacija z jedrom", imgTest)
    cv.waitKey(0)

    cv.destroyAllWindows()
    pass
