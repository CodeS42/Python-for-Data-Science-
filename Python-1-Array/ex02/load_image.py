from PIL import Image
from numpy import array


def ft_load(path: str) -> array:
    """
    Load an image from the given file path.
    Convert it to RGB.

    Parameters
        path: Path to the image file to load.

    Returns
        The loaded image as a 3D array.

    Raises
        TypeError: If the provided path is not a string.
        ValueError: If the image format is not JPG or JPEG.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")
        img = Image.open(path)
        format_img = img.format.upper()
        if not (format_img == "JPG" or format_img == "JPEG"):
            raise ValueError("Unsupported format.")
        img = img.convert("RGB")
        img_array = array(img)
        print(f"The shape of image is : {img_array.shape}")
        return img_array
    except Exception as e:
        print("Error: ", e)
        return None


def main():
    """

    """
    # Test subject
    print(ft_load("landscape.jpg"))
    print()

    # JPEG image
    print(ft_load("animal.jpeg"))
    print()

    # Wrong type of image
    print(ft_load("animal.j"))
    print()

    # Image doesn't exist
    print(ft_load("test.jpeg"))
    print()

    # Wrong type of input
    print(ft_load(1))

if __name__ == "__main__":
    main()
