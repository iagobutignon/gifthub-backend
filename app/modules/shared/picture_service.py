from io import BytesIO
import base64


class PictureService():
    def encode_image(image):
        buffered = BytesIO()
        image.save(buffered, format='JPEG')
        img = base64.b64encode(buffered.getvalue())
        return img

    def decode_image(image):
        img = BytesIO(base64.b64decode(image))
        return img
