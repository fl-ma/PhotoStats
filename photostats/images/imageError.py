
class ImageError(Exception):
    """Raised for errors during image processing

    Args:
        Error ([type]): [description]
    """
    def __init__(self, filename, message):
        self.filename = filename
        self.message  = message
        
class ExifError(ImageError):
    """Error during exif handling

    Args:
        ImageError ([type]): [description]
    """