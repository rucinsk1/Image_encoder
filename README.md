# Image_encoder
Simple app that allows user both: encoding text messanges in images and decoding hidden information from images.

## Encoding
Mode should be run in image_encoder repo folder
Running encoding mode:
```
python -m image_encoder --mode encoding --message <messagage_to_hide> --img-name <image_name>
```
- <message_to_hide> is a string, for example "test message"
- <image_name> is path to image which is already located in image_encoder/images folder. For example: test_image.png. If image exception will occur.

## Decoding
Mode should be run in image_encoder repo folder
Running decoding mode:
```
python -m image_encoder --mode decoding --img-name <image_name>
```
- <image_name> is path to image which is already located in image_encoder/images folder. For example: test_image.png. If image exception will occur.

