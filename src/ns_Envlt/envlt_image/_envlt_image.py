import dataclasses


@dataclasses.dataclass
class ImageSize:
    width: int
    height: int


class Image:
    def __init__(self, image_path: str, save_path: str):
        pass

    def resize_image(self, width: int, height: int):
        """
            缩放图片为指定大小

        :param width: 缩放后的宽
        :param height: 缩放后的高
        :return:
        """
        pass

    def get_image_size(self) -> ImageSize:
        """
            得到图片的分辨率

        :return: ImageSize类
        """
        pass
