import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from load_image import ft_load

def ft_invert(array) -> array:
    """
    Invert the colors of the image (255 - pixel)
    """
    new_img = np.zeros(array.shape, dtype=array.dtype)
    new_img = 255 - array
    plt.imshow(new_img)
    plt.show()

def ft_red(array) -> array:
    """
    Only keep the red channel: the others are set to zero.
    """
    new_img = np.zeros(array.shape, dtype=array.dtype)
    new_img[:, :, 0] = array[:, :, 0]
    new_img[:, :, 1] = 0
    new_img[:, :, 2] = 0
    plt.imshow(new_img)
    plt.show()

def ft_green(array) -> array:
    """
    Only keep the green channel: the others are set to zero.
    """
    new_img = np.zeros(array.shape, dtype=array.dtype)
    new_img[:, :, 0] = 0
    new_img[:, :, 1] = array[:, :, 1]
    new_img[:, :, 2] = 0
    plt.imshow(new_img)
    plt.show()

def ft_blue(array) -> array:
    """
    Only keep the blue channel: the others are set to zero.
    """
    new_img = np.zeros(array.shape, dtype=array.dtype)
    new_img[:, :, 0] = 0
    new_img[:, :, 1] = 0
    new_img[:, :, 2] = array[:, :, 2]
    plt.imshow(new_img)
    plt.show()


def ft_grey(array) -> array:
    """
    Converts the image to grayscale using the green channel.
    """
    new_img = np.zeros(array.shape, dtype=array.dtype)
    new_img[:, :, 0] = array[:, :, 1]
    new_img[:, :, 1] = array[:, :, 1]
    new_img[:, :, 2] = array[:, :, 1]
    plt.imshow(new_img)
    plt.show()

array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)