from PIL import Image
from pathlib import Path, PurePath
import os
from image_encoder.domain.logger import get_logger

logger = get_logger()

ENCODED_FILENAME_FORMAT = "{}_encoded.png"
IMAGES_PATH = PurePath(Path(os.path.dirname(os.path.realpath(__file__))).parent, 'images')
  
def read_image(img_name):

    #path to our image
    img_path = Path(PurePath(IMAGES_PATH, img_name))
    #check if image exists
    if not img_path.exists():
        raise Exception(f"Image {img_path} does not exist")

    #reading image
    image = Image.open(img_path, 'r')
    logger.debug(f'Image read properly!')
    return image

def save_image(image, image_name):
    new_img_name = ENCODED_FILENAME_FORMAT.format(image_name[:-4])
    if image_name == 'diff_image':
        new_img_name = 'diff_image.png'
    print(new_img_name)
    #images path
    images_path = PurePath(Path(os.path.dirname(os.path.realpath(__file__))).parent, 'images')
    image.save(Path(PurePath(images_path, new_img_name)))



