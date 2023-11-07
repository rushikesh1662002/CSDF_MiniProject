from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = 'Monalisa.jpg'
    extract_metadata(image_path)
