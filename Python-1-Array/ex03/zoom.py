from load_image import ft_load
from numpy import array
import matplotlib.pyplot as plt


def slice_me_3D(img, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """

    """
    try:
        if not all(isinstance(elem, int) for elem in (start_y, end_y, start_x, end_x, channel_start, channel_end)):
            raise TypeError("")
        new_img = img[start_y:end_y, start_x:end_x, channel_start:channel_end]
        new_img_shape = new_img.shape
        if len(new_img_shape) == 3 and new_img_shape[2] == 1:
            print(f"New shape after slicing: {new_img_shape} or {new_img_shape[:2]}")
        else:
            print(f"New shape after slicing: {new_img_shape}")
        return new_img
    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_zoom(img_array, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """

    """
    print(img_array)
    zoomed_img = slice_me_3D(img_array, start_y, end_y, start_x, end_x, channel_start, channel_end)
    print(zoomed_img)
    if zoomed_img.shape[2] == 1:
        plt.imshow(zoomed_img[:, :, 0], cmap="gray")
    else:
        plt.imshow(zoomed_img)
    plt.show()
    

def main():
    """

    """
    img = ft_load("animal.jpeg")
    ft_zoom(img, 100, 500, 450, 850, 0, 1)


if __name__ == "__main__":
    main()
