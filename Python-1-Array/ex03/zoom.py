from load_image import ft_load
from numpy import array
import matplotlib.pyplot as plt


def ft_zoom(img, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """
    Perform zoom on the image array and display it.

    Parameters:
        - img: numpy array of the loaded image
        - start_y, end_y, start_x, end_x, channel_start, channel_end: integers
        for slicing

    Prints:
        The sliced (zoomed) image array

    Displays:
        Zoomed image using matplotlib with grayscale
    """
    zoomed_img = img[start_y:end_y, start_x:end_x, channel_start:channel_end]
    zoomed_img_shape = zoomed_img.shape
    print(f"New shape after slicing: {zoomed_img_shape} or {zoomed_img_shape[:2]}")
    print(zoomed_img)
    plt.imshow(zoomed_img[:, :, 0], cmap="gray")
    plt.show()
    

def main():
    """
    Main function to load an image, display its information, and perform a zoom.

    - Loads 'animal.jpeg' using ft_load()
    - Prints the original image's shape and pixel values
    - Calls ft_zoom() with fixed slicing coordinates
    - Handles any exception and prints an error message
    """
    try:
        img = ft_load("animal.jpeg")
        print(f"The shape of image is : {img.shape}")
        print(img)
        ft_zoom(img, 100, 500, 450, 850, 0, 1)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
