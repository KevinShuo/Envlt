from envlt_image import Image

image = Image(r"C:\Users\wangshuo\Pictures\Screenshots\屏幕截图 2023-11-15 102317.png",
              r"C:\dev\maya\Envlt\src\envlt_image_rs\tests\aaa.png")
# 缩放图片分辨率
image.resize_image(960, 540)
# 获取图片分辨率
image_size = image.get_image_size()
print(f"width: {image_size.width} height: {image_size.height}")
