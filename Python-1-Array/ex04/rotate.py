from load_image import ft_load
import numpy
from numpy import array
import matplotlib.pyplot as plt


def ft_zoom(img, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """
    Slice a 3D image array according to given indices.

    Parameters:
        - img: numpy array representing the image
        - start_y, end_y: row indices for slicing (height)
        - start_x, end_x: column indices for slicing (width)
        - channel_start, channel_end: start and end indices for the channels

    Returns:
        new_img: sliced 2D image array

    Prints:
        Shape of the sliced image. If only one channel is selected, also shows
        the 2D equivalent shape.
    """
    new_img = img[start_y:end_y, start_x:end_x, channel_start:channel_end]
    new_img_shape = new_img.shape
    print(f"The shape of image is: {new_img_shape} or {new_img_shape[:2]}")
    print(new_img)
    return new_img[:, :, 0]


def ft_transpose(img):
    """
    Transpose a 2D image array, swapping its rows and columns.

    Parameters:
        img: The input image array with shape (height, width).

    Returns:
        None: The function prints the transposed image's shape and values,
              and displays the transposed image using matplotlib.

    Details:
        - Creates a new array with shape (width, height).
        - Copies the pixel values so that new_img[x, y] = img[y, x].
        - Prints the shape of the transposed image.
        - Prints the pixel values of the transposed image.
        - Displays the transposed image using a grayscale colormap.
    """
    new_img = numpy.zeros((img.shape[1], img.shape[0]), dtype=img.dtype)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            new_img[x, y] = img[y, x]
    print(f"New shape after Transpose: {new_img.shape}")
    print(new_img)
    plt.imshow(new_img, cmap="gray")
    plt.show()


def main():
    """
    Main function to load the image and perform zoom.

    - Loads 'animal.jpeg' using ft_load()
    - Calls ft_zoom() with fixed slicing coordinates
    - Calls ft_transpose() to rotate the sliced image.
    - Handles any exception and prints an error message
    """
    try:
        img = ft_load("animal.jpeg")
        zoomed_img = ft_zoom(img, 100, 500, 450, 850, 0, 1)
        ft_transpose(zoomed_img)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
