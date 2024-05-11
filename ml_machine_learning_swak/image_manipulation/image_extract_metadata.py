# EXIF data is metadata stored in image files. It contains information about the camera settings, date and time, etc.
from PIL import Image, JpegImagePlugin
from PIL.ExifTags import TAGS


def fetch_exif(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data is not None:
            # Convert EXIF data to a readable dictionary
            exif_dict = {TAGS[key]: exif_data[key] for key in exif_data.keys() if
                         key in TAGS and isinstance(exif_data[key], (int, str))}
            return exif_dict
        else:
            print("No EXIF data found in the image.")
            return None
    except Exception as e:
        print(f"Error fetching EXIF data: {e}")
        return None


def remove_exif(image_path, output_path):
    try:
        image = Image.open(image_path)
        image.save(output_path, exif="")
        print(f"EXIF data removed and saved to {output_path}")
    except Exception as e:
        print(f"Error removing EXIF data: {e}")


if __name__ == "__main__":

    data_repo = '../../data_repo/'
    image_path = f'{data_repo}pexels-pixabay-326900.jpg'

    # Fetch and print EXIF data
    exif_data = fetch_exif(image_path)
    if exif_data:
        print("EXIF Data:")
        for key, value in exif_data.items():
            print(f"{key}: {value}")

    # Remove EXIF data and save it on the same location
    remove_exif(image_path, image_path + '_noexif.png')
